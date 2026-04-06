from django.db import models

# Create your models here.
class newslatteremail(models.Model):
    userEmail = models.EmailField(max_length=254)

    def __str__(self):
        return self.userEmail