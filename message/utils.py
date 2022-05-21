from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage

def send_single_mail(to, subject, body):
    try:
        message = BaseEmailMessage(template_name="email/email.html", context={"body": body, 'subject': subject})
        message.send(to)
        # send_mail(recipient_list=to, from_email=settings.DEFAULT_FROM_EMAIL, subject=subject, message=body)
    except BadHeaderError:
        print("BadHEaderError occured.")
        return False
    return True
    