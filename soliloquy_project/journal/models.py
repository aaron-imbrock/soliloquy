from django.db import models
from django.urls import reverse

import datetime

# Create your models here.


class DayView(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateField(
        verbose_name="creation date", null=False, default=datetime.date.today
    )
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    day_of_week = models.TextChoices('DayOfWeek', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday')
    top_priorities = models.TextField()
    # TODO: this relationship can best be implemented w/ Postgres https://stackoverflow.com/a/66610526
    today_todos = models.ForeignKey(
        "Task",
        on_delete=models.CASCADE
    )
    hydration_log = models.TextField()
    meals_log = models.TextField()
    meditation_log = models.BooleanField(default=False)
    schedule = models.TextField()
    day_planning = models.TextField()
    day_review = models.TextField()

    def __str__(self):
        return str(self.date_created)

    def get_absolute_url(self):
        return reverse("day_detail", kwargs={"pk": self.pk})


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=60)
    date_created = models.DateField(
        verbose_name="creation date", null=True, default=datetime.date.today
    )
    date_complete = models.DateField(
        verbose_name="creation date", null=True, default=datetime.date.today
    )
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("todo", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['priority']
