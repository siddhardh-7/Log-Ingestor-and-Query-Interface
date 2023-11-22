from django.db import models


class Log(models.Model):
    level = models.CharField(max_length=255)
    message = models.TextField()
    resourceId = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    traceId = models.CharField(max_length=255)
    spanId = models.CharField(max_length=255)
    commit = models.CharField(max_length=255)
    parentResourceId = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.timestamp} - {self.message}"
