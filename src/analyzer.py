"""Data analysis module for financial insights"""

import pandas as pd
from typing import Dict, List


class FinancialAnalyzer:
    """Analyze financial data for reports"""

    def __init__(self, df):
        self.df = df

    def categorize_accounts(self):
        """Categorize accounts by type (Assets, Liabilities, Equity, Income, Expense)"""
        categories = {
            'Assets': [],
            'Liabilities': [],
            'Equity': [],
            'Income': [],
            'Expenses': []
        }
        return categories

    def calculate_totals(self):
        """Calculate totals by category"""
        try:
            totals = self.df.groupby('category')[['amount']].sum()
            return totals
        except Exception as e:
            print(f"Error calculating totals: {e}")
            return None

    def calculate_net_income(self, income_total: float, expense_total: float) -> float:
        """Calculate net income"""
        return income_total - expense_total

    def calculate_total_assets(self, current_assets: float, fixed_assets: float) -> float:
        """Calculate total assets"""
        return current_assets + fixed_assets

    def calculate_total_liabilities_equity(self, total_liabilities: float, total_equity: float) -> float:
        """Calculate total liabilities and equity"""
        return total_liabilities + total_equity

    def validate_accounting_equation(self, assets: float, liabilities: float, equity: float) -> bool:
        """Validate Assets = Liabilities + Equity"""
        tolerance = 0.01
        return abs(assets - (liabilities + equity)) < tolerance

    def get_summary(self) -> Dict:
        """Get financial summary"""
        summary = {
            'total_rows': len(self.df),
            'total_amount': self.df['amount'].sum() if 'amount' in self.df.columns else 0,
            'unique_accounts': self.df['account'].nunique() if 'account' in self.df.columns else 0
        }
        return summary
