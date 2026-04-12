from sqlmodel import SQLModel,Field
from datetime import datetime,date
from typing import Optional
from enum import Enum

class AccountType(str,Enum):
    ASSET = 'asset'
    LIABILITY = 'liability'
    EQUITY = 'equity'
    REVENUE = 'revenue'
    EXPENSE = 'expense'

class Account(SQLModel,table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    code: str = Field(unique=True)
    name: str
    account_type:AccountType
    parent_id:Optional[int] = None
    is_active:bool = True

class JournalEntry(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    date: date
    description:str
    reference_number:Optional[str]=None
    created_at:datetime = Field(default_factory=datetime.utcnow)

class TransactionLine(SQLModel,table=True):

    id:Optional[int] = Field(default=None,primary_key=True)
    journal_entry_id:int = Field(foreign_key='journalentry.id')
    account_id:int = Field(foreign_key='account.id')
    debit: float = 0.0
    credit: float = 0.0
    memo:Optional[str] = None