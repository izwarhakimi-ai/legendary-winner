# Accountant AI Tool

An AI-powered financial analysis tool for accountants that extracts financial data from emails, PDFs, and CSV files, processes them into structured formats, and generates professional financial reports including Balance Sheets and Profit & Loss statements.

## Features

- **Email Integration**: Access and extract PDF/CSV files from your email
- **Data Extraction**: Import data from PDF and CSV files
- **Data Processing**: Structure and normalize financial data
- **Financial Analysis**: Analyze transaction and account data
- **Report Generation**: Automatically create Balance Sheets and P&L statements

## Tech Stack

- Python 3.9+
- pandas - Data processing and analysis
- pdfplumber - PDF extraction
- openpyxl - Excel file generation
- python-dotenv - Environment configuration

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up `.env` file with your email credentials

## Usage

```bash
python main.py
```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── config/
│   └── config.py
├── src/
│   ├── __init__.py
│   ├── email_extractor.py
│   ├── data_processor.py
│   ├── analyzer.py
│   ├── financial_reports.py
│   └── utils.py
├── tests/
│   └── __init__.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
└── main.py
```
