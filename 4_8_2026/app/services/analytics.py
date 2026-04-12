from sqlmodel import Session, select, func
from app.models.transactions import TransactionLine,Account,AccountType,JournalEntry
from datetime import date

class AccountingAnalytics:
    
    def __init__(self,session:Session):
        self.session = session
    
    def get_account_balance(self,account:int) -> float:
        """
        Calculate running balance for an account
        """
        result = self.session.exec(
            select(
                func.coalesce(func.sum(TransactionLine.debit),0) -
                func.coalesce(func.sum(TransactionLine.credit),0)
            ).where(TransactionLine.account == account_id)
        ).first()
        return result or 0.0

    
    def get_trial_balance(self) -> list[dict]:
        """
        Generate trial balance report - all account with their balance
        """
        accounts = self.session.exec(select(Account)).all()
        trial_balance = []
        for account in accounts:
            balance = self.get_account_balance(account.id)
            trial_balance.append({
                'code':account.code,
                'name':account.name,
                'type':account.account_type,
                'debit_balance':balance if balance > 0 else 0,
                'credit_balance': abs(balance) if balance < 0 else 0,
            })
        
        return trial_balance
    
    def get_income_statement(self,start_date:date,end_date:date) -> dict:

        revenue = self._sum_by_type(AccountType.REVENUE,start_date,end_date)
        expenses = self._sum_by_type(AccountType.EXPENSE,start_date,end_date)
        return{
            'period':{'start':str(start_date),'end':str(end_date)},
            'total_revenue':revenue,
            'total_expenses':expenses,
            'net_income':revenue - expenses,
            'profit_margin':(revenue - expenses) / revenue * 100 if revenue else 0
        }

    
    def get_balance_sheet(self) -> dict:
        """ Snapshot of financial position"""
        assets = self._sum_by_type(AccountType.ASSET)
        liabilities = self._sum_by_type(AccountType.LIABILITY)
        equity = self._sum_by_type(AccountType.EQUITY)
        return{
            'assets':assets,
            'liabilities':liabilities,
            'equity':equity,
            'balanced':round(assets,2) == round(liabilities + equity,2)
        }

    def get_aging_report(self,as_of:date) -> dict:

        pass

    def _sum_by_type(self,account_type:AccountType,
            start_date: date = None, end_date:date = None
        ) -> float:
        query = (
            select(func.coalesce(
                func.sum(TransactionLine.credit) - func.sum(TransactionLine.debit),0
            ))
            .join(Account,TransactionLine.account_id == Account.id)
            .where(Account.account_type == account_type)
        )
        if start_date and end_date:
            query = query.join(
                JournalEntry, TransactionLine.journal_entry_id == JournalEntry.id
            ).where(JournalEntry.date.between(start_date,end_date))
        return self.session.exec(query).first() or 0