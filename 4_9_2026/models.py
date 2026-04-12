from sqlmodel import SQLModel,Field
from datetime import datetime
from typing import Optional


class Transaction(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    description:str
    amount:float
    category:str
    created_at:datetime = Field(default_factory=datetime.utcnow)


class Student(SQLModel,table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    first_name:str
    last_name:str
    email:str
    grade_level:str
    section:str
    status:str = 'Pending'
    created_at:datetime = Field(default_factor=datetime.utcnow)


class Course(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    name:str
    teacher:str
    schedule:str

class Enrollment(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    student_id:int = Field(foreign_key='student.id')
    course_id:int = Field(foreign_key='course.id')
    school_year:str
    status:str = 'Enrolled'
    created_at:datetime = Field(default_factory=datetime.utcnow)