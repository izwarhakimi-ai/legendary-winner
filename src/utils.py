"""Utility functions"""

import os
from config.config import FileConfig


def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        FileConfig.RAW_DATA_PATH,
        FileConfig.PROCESSED_DATA_PATH,
        FileConfig.REPORTS_PATH
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Ensured directory: {directory}")


def get_file_list(directory):
    """Get list of files in directory"""
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except Exception as e:
        print(f"Error getting file list: {e}")
        return []


def format_currency(value):
    """Format value as currency"""
    return f"${value:,.2f}"


def convert_to_float(value):
    """Convert value to float, handling various formats"""
    try:
        if isinstance(value, str):
            value = value.replace('$', '').replace(',', '')
        return float(value)
    except:
        return 0.0
