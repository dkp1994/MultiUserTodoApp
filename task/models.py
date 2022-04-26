from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todoapp(models.Model):
    status_choices = [
        ('C','😎'),
        ('P','🤕'),
    ]
    priority_choices = [
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    status = models.CharField(max_length=2, choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choices)

    def __str__(self):
        return str(self.user)