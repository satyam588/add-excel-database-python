from django.db import models

# Create your models here.

class Filedata(models.Model):
    id = models.IntegerField(primary_key=True)
    child_part_no = models.CharField(max_length=255)
    child_part_description = models.TextField()
    item_ref_number = models.TextField()
    quantity_production = models.CharField(max_length=255)
    created_on = models.DateField()

    def __str__(self) -> str:
        return self.child_part_no