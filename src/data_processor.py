"""Data processing module for importing and structuring financial data"""

import pandas as pd
import pdfplumber
import os
from config.config import FileConfig


class DataProcessor:
    """Process and structure financial data from various sources"""

    @staticmethod
    def read_csv(file_path):
        """Read CSV file"""
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return None

    @staticmethod
    def read_pdf(file_path):
        """Extract tables from PDF file"""
        try:
            all_tables = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    if tables:
                        for table in tables:
                            all_tables.append(pd.DataFrame(table[1:], columns=table[0]))
            return all_tables
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None

    @staticmethod
    def read_excel(file_path):
        """Read Excel file"""
        try:
            df = pd.read_excel(file_path)
            return df
        except Exception as e:
            print(f"Error reading Excel: {e}")
            return None

    @staticmethod
    def normalize_data(df):
        """Normalize and clean financial data"""
        try:
            # Remove empty rows and columns
            df = df.dropna(how='all')
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            # Convert numeric columns
            for col in df.columns:
                if 'amount' in col.lower() or 'value' in col.lower():
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            return df
        except Exception as e:
            print(f"Error normalizing data: {e}")
            return df

    @staticmethod
    def save_processed_data(df, output_filename):
        """Save processed data to structured CSV"""
        try:
            output_path = os.path.join(FileConfig.PROCESSED_DATA_PATH, output_filename)
            df.to_csv(output_path, index=False)
            print(f"Processed data saved to: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error saving processed data: {e}")
            return None

    @staticmethod
    def process_file(file_path):
        """Process file based on extension"""
        ext = file_path.split('.')[-1].lower()

        if ext == 'csv':
            df = DataProcessor.read_csv(file_path)
        elif ext == 'pdf':
            tables = DataProcessor.read_pdf(file_path)
            df = pd.concat(tables, ignore_index=True) if tables else None
        elif ext in ['xlsx', 'xls']:
            df = DataProcessor.read_excel(file_path)
        else:
            print(f"Unsupported file type: {ext}")
            return None

        if df is not None:
            df = DataProcessor.normalize_data(df)
            filename = os.path.basename(file_path)
            output_name = f"processed_{filename.rsplit('.', 1)[0]}.csv"
            return DataProcessor.save_processed_data(df, output_name)

        return None
