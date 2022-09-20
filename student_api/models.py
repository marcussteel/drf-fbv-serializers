from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"

class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    # blank true : admin panelde bunu boş bırakabilirsn, null true ise database de bunu boş bırakabilirsin

    def __str__(self):
        return f"{self.last_name} {self.first_name}"