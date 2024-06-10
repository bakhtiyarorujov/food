from django.db import models
from .validators import validate_gmail

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField('Ad', max_length=100, unique=True)
    email = models.EmailField('E-poct')
    subject = models.CharField('Movzu', max_length= 150)
    message = models.TextField('Mesaj')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self) -> str:
        return f'{self.subject} - {self.name}'