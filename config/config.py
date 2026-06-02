import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

class EmailConfig:
    """Email configuration"""
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    IMAP_SERVER = os.getenv('EMAIL_IMAP_SERVER', 'imap.gmail.com')
    IMAP_PORT = int(os.getenv('EMAIL_IMAP_PORT', 993))

class FileConfig:
    """File processing configuration"""
    RAW_DATA_PATH = 'data/raw/'
    PROCESSED_DATA_PATH = 'data/processed/'
    REPORTS_PATH = 'data/reports/'
    ALLOWED_FILE_TYPES = ['pdf', 'csv', 'xlsx']
