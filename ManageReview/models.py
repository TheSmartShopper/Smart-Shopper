from django.db import models


class Review(models.Model):
    text = models.TextField(max_length=1024, default="", blank=True, null=True)
    rating = models.PositiveIntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), blank=False, null=False)
