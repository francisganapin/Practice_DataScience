from fastapi import APIRouter,Depends,Query
from sqlmodel import Session
from app.database import get_session
from app.services.analytics import AccountingAnalytics
from datetime import date 

router = APIRouter(prefix='/api/reports',tags=['Reports'])

@router.get('/trial-balance')
def trial_balance(session: Session = Depends(get_session)):
    analytics = AccountingAnalytics(sessions)
    return analytics.get_trial_balance()

@router.get('/income-statement')
def income_statement(
    start_date:date = Query(...),
    end_date: date = Query(...),
    session:Session = Depends(get_session)
    ):
    analytics = AccountingAnalytics(session)
    return analytics.get_income_statement(start_date,end_date)


@router.get('/balance-sheet')
def balance_sheet(session:Session = Depends(get_session)):
    analytics = AccountingAnalytics(session)
    return analytics.get_balance_sheet()


@router.get('/dashboard')
def dashboard_summary(session:Session = Depends(get_session)):

    analytics = AccountingAnalytics(session)
    today = date.today()
    first_of_month = today.replace(day=1)

    return {
        'balance_sheet':analytics.get_balance_sheet(),
        'monthly_pnl':analytics.get_income_statement(first_of_month,today),
        'generated_at':today.isoformat()
    }