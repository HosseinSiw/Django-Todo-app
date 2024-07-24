from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from .models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Assuming you have templates for the email content
        plaintext = get_template('users/email/welcome.txt')
        html = get_template('users/email/welcome.html')

        d = {'username': instance.username}

        text_content = plaintext.render(d)
        html_content = html.render(d)

        subject = 'Welcome to MyApp!'
        from_email = settings.EMAIL_HOST_USER
        to = instance.email

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")

        try:
            msg.send()
        except Exception as e:
            print(f"Failed to send email: {e}")
