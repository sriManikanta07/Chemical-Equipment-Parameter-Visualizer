from django.db import models
from django.contrib.auth.models import User

class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
   


    # STATS
    total_records = models.IntegerField(default=0)
    avg_flowrate = models.FloatField(default=0)
    avg_pressure = models.FloatField(default=0)
    avg_temperature = models.FloatField(default=0)
    type_distribution = models.JSONField(default=dict)
    per_type_stats = models.JSONField(default=dict)
   
    def __str__(self):
        return self.file_name
