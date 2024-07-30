# portal/models.py
from django.db import models

class CaptivePortalContent(models.Model):
    image = models.ImageField(upload_to='portal_images/', blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.message[:50]  # Display the first 50 characters of the message in the admin

