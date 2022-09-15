from ctypes import Union
from pathlib import WindowsPath
from typing import List
from helpers import dostify

@dostify(errors=[(ValueError,'')])
def send_gmail_using_app_password(gmail_username:str, gmail_app_password:str, to_email_id:Union[str, List[str]], subject:str, message:str, attachment_path:Union[WindowsPath, List[WindowsPath]]):
    # Import Section
    import os
    from my_dost.CrashHandler import report_error
    from pathlib import Path
    import yagmail

    # Validation Section
    if not gmail_username:
        raise ValueError(f'Gmail username cannot be empty')

    if not gmail_app_password:
        raise ValueError(f'Gmail app password cannot be empty')

    if not to_email_id:
        raise ValueError(f'To email id cannot be empty')

    if not subject:
        raise ValueError(f'Subject cannot be empty')

    if not message:
        raise ValueError(f'Message cannot be empty')

    yag = yagmail.SMTP(gmail_username, gmail_app_password)

    if attachment_path:
        yag.send(to_email_id, subject, message,
                    attachments=attachment_path)
    else:
        yag.send(to=to_email_id, subject=subject, contents=message)

        # Alternatively, with a simple one-liner:
        # yagmail.SMTP(gmail_username).send(to_email_id, subject, message)