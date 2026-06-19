from sqlalchemy import Column,Integer,String,DateTime,Text,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base






class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer,primary_key=True, index = True)

    title = Column(String,nullable=False)
    description = Column(Text)

    assigned_to = Column(String, nullable=False)
    created_by = Column(String, nullable= False)

    priority = Column(String, nullable=False)

    due_date = Column(DateTime, nullable=False)

    category = Column(String)

    status = Column(String, default="Pending")

    created_at = Column(DateTime, default=datetime.now)

    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    completed_at = Column(DateTime, nullable=True)

    comments = relationship(
        "Comment",
        back_populates="task"
    )

    histories = relationship(
        "TaskHistory",
        back_populates="task"
    )


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)

    task_id = Column(
        Integer,
        ForeignKey("tasks.id")
    )

    message = Column(Text)

    added_by = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.now
    )

    task = relationship(
        "Task",
        back_populates="comments"
    )


class TaskHistory(Base):
    __tablename__ = "task_history"

    id = Column(Integer, primary_key=True)

    task_id = Column(
        Integer,
        ForeignKey("tasks.id")
    )

    old_status = Column(String)

    new_status = Column(String)

    changed_by = Column(String)

    changed_at = Column(
        DateTime,
        default=datetime.now
    )

    task = relationship(
        "Task",
        back_populates="histories"
    )
    
    

