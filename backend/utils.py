from django.core.mail import send_mail


class Util:
    @staticmethod
    def sent_email(data, email):
        # email = EmailMessage(
        #     subject=data['email_subject'],
        #     body=data['email_body']
        # ),
        # email.send()
        send_mail(data['email_subject'], data['email_body'], 'info@sonu.com', [email])
