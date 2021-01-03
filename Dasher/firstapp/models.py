from django.db import models

# Create your models here.
class Travel(models.Model):
    awb_num = models.IntegerField()
    carrier = models.CharField(max_length = 20)
    cur_status = models.CharField(max_length = 50)
    code = models.CharField(max_length = 4)
    ETD = models.CharField(max_length = 70)
    source = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 20)
    scandata = models.JSONField()

    def __str__(self):
        return str(self.awb_num)
        