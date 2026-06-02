#!/usr/bin/env python3
"""Main entry point for Accountant AI Tool"""

import os
from src.email_extractor import EmailExtractor
from src.data_processor import DataProcessor
from src.analyzer import FinancialAnalyzer
from src.financial_reports import FinancialReportGenerator
from src.utils import ensure_directories, get_file_list
from config.config import FileConfig


def main():
    """Main application flow"""
    print("="*60)
    print("  Accountant AI Tool - Financial Analysis System")
    print("="*60)

    # Ensure directories exist
    ensure_directories()

    # Menu
    while True:
        print("\nOptions:")
        print("1. Extract files from email")
        print("2. Process file (CSV/PDF/Excel)")
        print("3. Generate financial reports")
        print("4. View processed files")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == '1':
            extract_from_email()
        elif choice == '2':
            process_file()
        elif choice == '3':
            generate_reports()
        elif choice == '4':
            view_files()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


def extract_from_email():
    """Extract files from email"""
    print("\n--- Extract Files from Email ---")
    extractor = EmailExtractor()

    if extractor.connect():
        files = extractor.extract_attachments()
        print(f"Extracted {len(files)} file(s)")
        extractor.disconnect()
    else:
        print("Failed to connect to email. Check your credentials in .env")


def process_file():
    """Process a financial data file"""
    print("\n--- Process File ---")
    files = get_file_list(FileConfig.RAW_DATA_PATH)

    if not files:
        print("No files in raw data folder.")
        return

    print("\nAvailable files:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    try:
        choice = int(input("Select file number: ")) - 1
        file_path = os.path.join(FileConfig.RAW_DATA_PATH, files[choice])
        DataProcessor.process_file(file_path)
    except (ValueError, IndexError):
        print("Invalid selection.")


def generate_reports():
    """Generate financial reports"""
    print("\n--- Generate Financial Reports ---")
    print("This feature requires financial data input.")
    print("Sample data mode - using example values...\n")

    # Example data (replace with actual processed data)
    sample_data = {
        'current_assets': 50000,
        'fixed_assets': 100000,
        'current_liabilities': 30000,
        'long_term_liabilities': 50000,
        'equity': 70000,
        'revenue': 500000,
        'cogs': 250000,
        'operating_expenses': 100000,
        'other_income': 5000,
        'other_expenses': 2000,
        'tax_expense': 30000
    }

    analyzer = FinancialAnalyzer(None)
    generator = FinancialReportGenerator(analyzer)

    # Generate Balance Sheet
    bs = generator.generate_balance_sheet(
        sample_data['current_assets'],
        sample_data['fixed_assets'],
        sample_data['current_liabilities'],
        sample_data['long_term_liabilities'],
        sample_data['equity']
    )

    # Generate P&L Statement
    pl = generator.generate_profit_loss(
        sample_data['revenue'],
        sample_data['cogs'],
        sample_data['operating_expenses'],
        sample_data['other_income'],
        sample_data['other_expenses'],
        sample_data['tax_expense']
    )

    print("--- Balance Sheet ---")
    print(bs.to_string())

    print("\n--- Profit & Loss Statement ---")
    print(pl.to_string())

    # Save reports
    generator.save_report(bs, 'balance_sheet')
    generator.save_report(pl, 'profit_loss')


def view_files():
    """View available files in directories"""
    print("\n--- View Files ---")

    print("\nRaw files:")
    raw_files = get_file_list(FileConfig.RAW_DATA_PATH)
    for f in raw_files:
        print(f"  - {f}")

    print("\nProcessed files:")
    processed_files = get_file_list(FileConfig.PROCESSED_DATA_PATH)
    for f in processed_files:
        print(f"  - {f}")

    print("\nReports:")
    report_files = get_file_list(FileConfig.REPORTS_PATH)
    for f in report_files:
        print(f"  - {f}")


if __name__ == '__main__':
    main()
