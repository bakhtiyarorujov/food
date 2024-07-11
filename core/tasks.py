from celery import shared_task
import time
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from stories.models import Receipe
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

User = get_user_model()


@shared_task
def export_data():
    print('Export started ...')
    time.sleep(10)
    print('Export ended ...')

@shared_task
def send_email_to_users():
    email_list = User.objects.values_list('email', flat=True)
    recipes = Receipe.objects.all()[:3]
    message = render_to_string('email.html', {
        "recipes": recipes
    })
    subject = 'New Recipes'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()

"""
python -m celery -A food_stories  worker -l INFO
celery -A [project-name] worker --beat --scheduler django --loglevel=info
"""