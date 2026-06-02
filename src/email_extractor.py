"""Email extraction module for accessing and extracting files from email"""

import imaplib
import email
from email.header import decode_header
import os
from config.config import EmailConfig, FileConfig


class EmailExtractor:
    """Extract PDF and CSV files from email"""

    def __init__(self):
        self.email_address = EmailConfig.EMAIL_ADDRESS
        self.password = EmailConfig.EMAIL_PASSWORD
        self.imap_server = EmailConfig.IMAP_SERVER
        self.imap_port = EmailConfig.IMAP_PORT
        self.mail = None

    def connect(self):
        """Connect to email server"""
        try:
            self.mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            self.mail.login(self.email_address, self.password)
            print(f"Connected to {self.imap_server}")
            return True
        except Exception as e:
            print(f"Failed to connect to email: {e}")
            return False

    def disconnect(self):
        """Disconnect from email server"""
        if self.mail:
            self.mail.close()
            self.mail.logout()

    def extract_attachments(self, folder='INBOX', file_types=None):
        """Extract attachments from emails"""
        if not file_types:
            file_types = FileConfig.ALLOWED_FILE_TYPES

        extracted_files = []

        try:
            self.mail.select(folder)
            status, messages = self.mail.search(None, 'ALL')

            for msg_id in messages[0].split():
                status, msg_data = self.mail.fetch(msg_id, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])

                # Process attachments
                for part in msg.walk():
                    if part.get_content_disposition() == 'attachment':
                        filename = part.get_filename()
                        if filename:
                            file_ext = filename.split('.')[-1].lower()
                            if file_ext in file_types:
                                file_path = os.path.join(FileConfig.RAW_DATA_PATH, filename)
                                with open(file_path, 'wb') as f:
                                    f.write(part.get_payload(decode=True))
                                extracted_files.append(file_path)
                                print(f"Extracted: {filename}")

        except Exception as e:
            print(f"Error extracting attachments: {e}")

        return extracted_files

    def search_emails_by_subject(self, subject, folder='INBOX'):
        """Search emails by subject and extract attachments"""
        try:
            self.mail.select(folder)
            status, messages = self.mail.search(None, f'SUBJECT "{subject}"')
            return messages[0].split()
        except Exception as e:
            print(f"Error searching emails: {e}")
            return []
