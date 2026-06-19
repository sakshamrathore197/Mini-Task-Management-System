from fastapi import FastAPI, Request, Depends,Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from datetime import datetime
from fastapi import Query



from .database import engine, get_db
from . import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

#Dashboard
@app.get("/")
def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):

    total_tasks = db.query(
        models.Task
    ).count()

    pending_tasks = db.query(
        models.Task
    ).filter(
        models.Task.status == "Pending"
    ).count()

    in_progress = db.query(
        models.Task
    ).filter(
        models.Task.status == "In Progress"
    ).count()

    completed = db.query(
        models.Task
    ).filter(
        models.Task.status == "Completed"
    ).count()

    overdue = db.query(
        models.Task
    ).filter(
        models.Task.due_date < datetime.now(),
        models.Task.status != "Completed",
        models.Task.status != "Cancelled"
    ).count()

    high_priority = db.query(
        models.Task
    ).filter(
        models.Task.priority.in_(["High", "Urgent"])
    ).count()

    latest_tasks = db.query(
        models.Task
    ).order_by(
        models.Task.created_at.desc()
    ).limit(5).all()

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "total_tasks": total_tasks,
            "pending_tasks": pending_tasks,
            "in_progress": in_progress,
            "completed": completed,
            "overdue": overdue,
            "high_priority": high_priority,
            "latest_tasks": latest_tasks
        }
    )



#add task
@app.get("/add-task")
def add_task_page(request:Request):
    return templates.TemplateResponse(
        "add_task.html",
        {
            'request':request
        }
    )


@app.post("/add-task")
def create_task(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    assigned_to: str = Form(...),
    created_by: str = Form(...),
    priority: str = Form(...),
    due_date: str = Form(...),
    category: str = Form(...),
    db: Session = Depends(get_db)
):

    # Required field validations

    if not title.strip():
        return templates.TemplateResponse(
            "add_task.html",
            {
                "request": request,
                "error": "Task Title is required."
            }
        )

    if not assigned_to.strip():
        return templates.TemplateResponse(
            "add_task.html",
            {
                "request": request,
                "error": "Please select assigned person."
            }
        )

    if not priority:
        return templates.TemplateResponse(
            "add_task.html",
            {
                "request": request,
                "error": "Please select task priority."
            }
        )

    # Duplicate Task Validation

    existing_task = db.query(
        models.Task
    ).filter(
        models.Task.title == title,
        models.Task.assigned_to == assigned_to,
        models.Task.status != "Completed"
    ).first()

    if existing_task:
        return templates.TemplateResponse(
            "add_task.html",
            {
                "request": request,
                "error":
                "Similar active task already exists for this user."
            }
        )

    task = models.Task(
        title=title,
        description=description,
        assigned_to=assigned_to,
        created_by=created_by,
        priority=priority,
        due_date=datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ),
        category=category
    )

    db.add(task)
    db.commit()

    return RedirectResponse(
        url="/tasks",
        status_code=303
    )

#Task List Page
@app.get("/tasks")
def task_list(
    request: Request,
    search: str = "",
    status: str = "",
    priority: str = "",
    category: str = "",
    db: Session = Depends(get_db)
):

    tasks_query = db.query(models.Task)

    # Search by title
    if search:
        tasks_query = tasks_query.filter(
            models.Task.title.ilike(f"%{search}%")
        )

    # Filter by status
    if status:
        tasks_query = tasks_query.filter(
            models.Task.status == status
        )

    # Filter by priority
    if priority:
        tasks_query = tasks_query.filter(
            models.Task.priority == priority
        )

    # Filter by category
    if category:
        tasks_query = tasks_query.filter(
            models.Task.category == category
        )

    tasks = tasks_query.all()

    return templates.TemplateResponse(
        "task_list.html",
        {
            "request": request,
            "tasks": tasks,
            "search": search,
            "status": status,
            "priority": priority,
            "category": category
        }
    )

#TaskDetails
@app.get("/task/{task_id}")
def task_detail(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    

    task = db.query(
        models.Task
        ).filter(
            models.Task.id == task_id
            ).first()

    comments = db.query(
        models.Comment
        ).filter(
            models.Comment.task_id == task_id
            ).order_by(
                models.Comment.created_at.desc()
                ).all()
    

    histories = db.query(
        models.TaskHistory
        ).filter(
            models.TaskHistory.task_id == task_id
            ).order_by(
                models.TaskHistory.changed_at.desc()
                ).all()

    return templates.TemplateResponse(
        "task_detail.html",
        {
            "request": request,
            "task": task,
            "comments":comments
        }
    )


#TaskDetailsComment
@app.post("/task/{task_id}/comment")
def add_comment(
    task_id: int,
    message: str = Form(...),
    added_by: str = Form(...),
    db: Session = Depends(get_db)
):

    comment = models.Comment(
        task_id=task_id,
        message=message,
        added_by=added_by
    )

    db.add(comment)
    db.commit()

    return RedirectResponse(
        url=f"/task/{task_id}",
        status_code=303
    )

#Status Update Route
@app.post("/task/{task_id}/status")
def update_task_status(
    task_id: int,
    new_status: str = Form(...),
    changed_by: str = Form(...),
    db: Session = Depends(get_db)
):

    task = db.query(
        models.Task
    ).filter(
        models.Task.id == task_id
    ).first()
    if task.status == "Completed":
        return {
        "message":
        "Completed task cannot be updated unless reopened."
    }

    if not task:
        return {"message": "Task not found"}

    # Store current status
    old_status = task.status

    # Create history record
    history = models.TaskHistory(
        task_id=task.id,
        old_status=old_status,
        new_status=new_status,
        changed_by=changed_by
    )

    db.add(history)

    # Update task status
    task.status = new_status

    if new_status == "Completed":
        task.completed_at = datetime.now()

    db.commit()

    return RedirectResponse(
        url=f"/task/{task_id}",
        status_code=303
    )
