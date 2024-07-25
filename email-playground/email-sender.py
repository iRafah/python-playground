import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Joe Doe'
email['to'] = 'joe-doe@gmail.com'
email['subject'] = 'Python Fun. Sending emails via Python!'

email.set_content(html.substitute(name='Tin Tin'), 'html')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('joedoe@outlook.com', 'pass')
    smtp.send_message(email)
    print('All good!')
