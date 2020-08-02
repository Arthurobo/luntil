from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, help_text='Name of Sender')
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.name
