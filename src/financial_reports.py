"""Financial report generation module"""

import pandas as pd
from datetime import datetime
from config.config import FileConfig
import os


class FinancialReportGenerator:
    """Generate Balance Sheet and P&L statements"""

    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.timestamp = datetime.now().strftime("%Y-%m-%d")

    def generate_balance_sheet(self, current_assets: float, fixed_assets: float,
                             current_liabilities: float, long_term_liabilities: float,
                             equity: float) -> pd.DataFrame:
        """Generate balance sheet"""

        total_assets = current_assets + fixed_assets
        total_liabilities = current_liabilities + long_term_liabilities
        total_liabilities_equity = total_liabilities + equity

        balance_sheet = {
            'ASSETS': ['', 'Current Assets', f'{current_assets:,.2f}', '', 'Fixed Assets', f'{fixed_assets:,.2f}', '', 'TOTAL ASSETS', f'{total_assets:,.2f}'],
            'LIABILITIES & EQUITY': ['', 'Current Liabilities', f'{current_liabilities:,.2f}', '', 'Long-term Liabilities', f'{long_term_liabilities:,.2f}', '', 'Equity', f'{equity:,.2f}', 'TOTAL LIABILITIES & EQUITY', f'{total_liabilities_equity:,.2f}']
        }

        df = pd.DataFrame(balance_sheet)
        return df

    def generate_profit_loss(self, revenue: float, cost_of_goods_sold: float,
                            operating_expenses: float, other_income: float,
                            other_expenses: float, tax_expense: float) -> pd.DataFrame:
        """Generate profit and loss statement"""

        gross_profit = revenue - cost_of_goods_sold
        operating_income = gross_profit - operating_expenses
        other_net = other_income - other_expenses
        earnings_before_tax = operating_income + other_net
        net_income = earnings_before_tax - tax_expense

        pl_statement = {
            'Item': [
                'Revenue',
                'Cost of Goods Sold',
                'Gross Profit',
                'Operating Expenses',
                'Operating Income',
                'Other Income',
                'Other Expenses',
                'Earnings Before Tax',
                'Tax Expense',
                'Net Income'
            ],
            'Amount': [
                f'{revenue:,.2f}',
                f'{cost_of_goods_sold:,.2f}',
                f'{gross_profit:,.2f}',
                f'{operating_expenses:,.2f}',
                f'{operating_income:,.2f}',
                f'{other_income:,.2f}',
                f'{other_expenses:,.2f}',
                f'{earnings_before_tax:,.2f}',
                f'{tax_expense:,.2f}',
                f'{net_income:,.2f}'
            ]
        }

        df = pd.DataFrame(pl_statement)
        return df

    def save_report(self, df, report_type, format='csv'):
        """Save report to file"""
        try:
            filename = f"{report_type}_{self.timestamp}.{format}"
            filepath = os.path.join(FileConfig.REPORTS_PATH, filename)

            if format == 'csv':
                df.to_csv(filepath, index=False)
            elif format == 'xlsx':
                df.to_excel(filepath, index=False)

            print(f"Report saved: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error saving report: {e}")
            return None
