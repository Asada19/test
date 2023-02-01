from django.db import models


class ValueForInput(models.Model):
    value = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.value
