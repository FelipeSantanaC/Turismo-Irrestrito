from django.db import models

class Preferencia(models.Model):
    cluster_id = models.IntegerField()
    local1 = models.IntegerField()
    local2 = models.IntegerField()
    local3 = models.IntegerField()
    local4 = models.IntegerField()

    def __str__(self):
        return f"Preferencia do Cluster {self.cluster_id}"
