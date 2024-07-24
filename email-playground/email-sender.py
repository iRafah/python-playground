import smtplib

from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Joe Doe'
email['to'] = 'joe-doe@hotmail.com'
email['subject'] = 'Python Fun. Sending emails via Python!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('joedoe@outlook.com', 'pass')
    smtp.send_message(email)
    print('All good!')
