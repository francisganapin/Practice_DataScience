from fastapi import FastAPI,Depends
from sqlmodel import Session,select
from database import create_db_and_tables,get_session
from models import Transaction

app = FastAPI()


@app.on_event('startup')
def on_startup():
    create_db_and_tables()



@app.post('/transactions')
def create_transaction(transaction:Transaction,session:Session = Depends(get_session)):
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return transaction




@app.get('/transactions')
def get_all_transaction(session:Session = Depends(get_session)):
    transaction = session.exec(select(Transaction)).all()
    return transaction



@app.get('/dashboard')
def dashboard(session:Session = Depends(get_session)):
    transaction = session.exec(select(Transaction)).all()
    total_income = sum(t.amount for t in transaction if t.category == 'Income')
    total_expense = sum(t.amount for t in transaction if t.category == 'Expense')
    balance = total_income - total_expense
    return {
        "total_income":total_income,
        "total_expense":total_expense,
        "balance":balance,
        "transaction_count":len(transaction)
    }




@app.post('api/v1/create/student')
