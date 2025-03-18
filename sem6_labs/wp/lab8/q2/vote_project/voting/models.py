# voting/models.py
from django.db import models

class BookVote(models.Model):
    GOOD = 'Good'
    SATISFACTORY = 'Satisfactory'
    BAD = 'Bad'

    CHOICE = [
        (GOOD, 'Good'),
        (SATISFACTORY, 'Satisfactory'),
        (BAD, 'Bad'),
    ]

    choice = models.CharField(max_length=50, choices=CHOICE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
