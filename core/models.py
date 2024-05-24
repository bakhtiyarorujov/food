from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField('Ad', max_length=100)
    email = models.EmailField('E-poct')
    subject = models.CharField('Movzu', max_length= 150)
    meesage = models.TextField('Mesaj')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self) -> str:
        return f'{self.subject} - {self.name}'