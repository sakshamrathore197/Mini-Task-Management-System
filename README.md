# Mini Task Management System

## Short Project Description

Mini Task Management System is a web-based application developed using FastAPI that allows managers to create, assign, track, and manage tasks assigned to team members. The system helps organizations monitor task progress, maintain activity history, and improve daily productivity through a centralized dashboard.

---

## Features Implemented

### Core Features

* Dashboard with task statistics
* Add new task
* View all tasks
* Task detail page
* Assign tasks to team members
* Update task status
* Add task comments/updates
* Task status history tracking
* Search tasks by title
* Filter tasks by status, priority, and category
* Dashboard overdue task count
* High priority task count

### Validation Features

* Required field validation
* Duplicate active task validation
* Completed task update restriction

### UI Features

* Responsive user interface
* Navigation menu
* Dashboard cards
* Styled tables and forms
* Status and priority indicators

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to project directory

```bash
cd mini-task-management-system
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

---

## Run Instructions

Start the application using:

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

---

## Test Login Details

No authentication/login system has been implemented in this version of the application.

---

## Important Notes

* The application uses SQLite as the database.
* Database file (`task.db`) is automatically created during the first run.
* If database schema changes, delete the existing `task.db` file and restart the application.
* Ensure the virtual environment is activated before running the project.
* The project is developed for demonstration and learning purposes and can be extended further with authentication, notifications, file uploads, and reporting features.

---

## Technology Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Server:** Uvicorn

---

## Project Structure

```text
mini_task_management/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── templates/
│   └── static/
│
├── task.db
├── requirements.txt
└── README.md
```
# Mini Task Management System

## Short Project Description

Mini Task Management System is a web-based application developed using FastAPI that allows managers to create, assign, track, and manage tasks assigned to team members. The system helps organizations monitor task progress, maintain activity history, and improve daily productivity through a centralized dashboard.

---

## Features Implemented

### Core Features

* Dashboard with task statistics
* Add new task
* View all tasks
* Task detail page
* Assign tasks to team members
* Update task status
* Add task comments/updates
* Task status history tracking
* Search tasks by title
* Filter tasks by status, priority, and category
* Dashboard overdue task count
* High priority task count

### Validation Features

* Required field validation
* Duplicate active task validation
* Completed task update restriction

### UI Features

* Responsive user interface
* Navigation menu
* Dashboard cards
* Styled tables and forms
* Status and priority indicators

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to project directory

```bash
cd mini-task-management-system
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

---

## Run Instructions

Start the application using:

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

---

## Test Login Details

No authentication/login system has been implemented in this version of the application.

---

## Important Notes

* The application uses SQLite as the database.
* Database file (`task.db`) is automatically created during the first run.
* If database schema changes, delete the existing `task.db` file and restart the application.
* Ensure the virtual environment is activated before running the project.
* The project is developed for demonstration and learning purposes and can be extended further with authentication, notifications, file uploads, and reporting features.

---

## Technology Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Server:** Uvicorn

---

## Project Structure

```text
mini_task_management/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── templates/
│   └── static/
│
├── task.db
├── requirements.txt
└── README.md
```
