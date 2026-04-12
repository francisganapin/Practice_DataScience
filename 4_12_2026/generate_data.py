import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_accounting_data():
    np.random.seed(42) # For reproducibility
    
    # Setup some basic accounts
    accounts = {
        '1000': {'name': 'Cash', 'category': 'Asset'},
        '1200': {'name': 'Accounts Receivable', 'category': 'Asset'},
        '2000': {'name': 'Accounts Payable', 'category': 'Liability'},
        '3000': {'name': 'Owner Equity', 'category': 'Equity'},
        '4000': {'name': 'Sales Revenue', 'category': 'Revenue'},
        '5000': {'name': 'Rent Expense', 'category': 'Expense'},
        '5100': {'name': 'Salary Expense', 'category': 'Expense'},
        '5200': {'name': 'Office Supplies', 'category': 'Expense'}
    }

    start_date = datetime(2026, 4, 1)
    data = []
    transaction_id = 100

    # Generate 50 random transactions (each needs a debit and a credit)
    for _ in range(50):
        date = start_date + timedelta(days=np.random.randint(0, 30))
        amount = round(np.random.uniform(50, 5000), 2)
        
        # Randomly choose a transaction scenario
        scenario = np.random.choice(['Sale_Cash', 'Sale_Credit', 'Pay_Rent', 'Pay_Salary', 'Buy_Supplies'])
        
        if scenario == 'Sale_Cash':
            dr_acc, cr_acc = '1000', '4000'
            desc = "Cash sale to customer"
        elif scenario == 'Sale_Credit':
            dr_acc, cr_acc = '1200', '4000'
            desc = "Invoice sent to customer"
        elif scenario == 'Pay_Rent':
            dr_acc, cr_acc = '5000', '1000'
            desc = "Monthly rent payment"
        elif scenario == 'Pay_Salary':
            dr_acc, cr_acc = '5100', '1000'
            desc = "Employee salary payout"
        else: # Buy_Supplies
            dr_acc, cr_acc = '5200', '2000'
            desc = "Bought supplies on credit"

        # DEBIT Entry
        data.append({
            'Transaction_ID': f'TXN-{transaction_id}',
            'Date': date.strftime('%Y-%m-%d'),
            'Account_ID': dr_acc,
            'Account_Name': accounts[dr_acc]['name'],
            'Category': accounts[dr_acc]['category'],
            'Description': desc,
            'Debit': amount,
            'Credit': 0.0
        })
        
        # CREDIT Entry
        data.append({
            'Transaction_ID': f'TXN-{transaction_id}',
            'Date': date.strftime('%Y-%m-%d'),
            'Account_ID': cr_acc,
            'Account_Name': accounts[cr_acc]['name'],
            'Category': accounts[cr_acc]['category'],
            'Description': desc,
            'Debit': 0.0,
            'Credit': amount
        })
        
        transaction_id += 1

    df = pd.DataFrame(data)
    # Sort by date and transaction ID
    df = df.sort_values(by=['Date', 'Transaction_ID']).reset_index(drop=True)
    df.to_csv('accounting_journal.csv', index=False)
    print("Created 'accounting_journal.csv' successfully!")

generate_accounting_data()
