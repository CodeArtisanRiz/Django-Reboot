from django.db import models
from django.utils import timezone

# Create your models here.
class TeaTypes(models.Model):
    TEA_TYPE_CHOICES = (
        ('BT', 'Black Tea'),
        ('GT', 'Green Tea'),
        ('HT', 'Herbal Tea'),
        ('OT', 'Oolong Tea'),
        ('PT', 'Pu-erh Tea'),
        ('WT', 'White Tea'),
    )
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tea_images/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=TEA_TYPE_CHOICES)
    price = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.name
