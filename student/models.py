from django.db import models

# Create your models here.
class Studentmodel(models.Model):
    stid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=100)

    def __str__(self):
        return self.stname

class Markmodel(models.Model):
    marksid = models.IntegerField(primary_key=True)
    maths = models.IntegerField()
    physics = models.IntegerField()
    computers = models.IntegerField()
    stid = models.ForeignKey(Studentmodel, related_name='marks', on_delete=models.CASCADE)