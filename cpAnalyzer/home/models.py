from django.db import models

# Create your models here.
class Member(models.Model):
    rollNo = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    codechef_user = models.CharField(max_length=50)
    codeforces_user = models.CharField(max_length=50)
    leetcode_user = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.rollNo