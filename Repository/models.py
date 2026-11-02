
from django.db import models

class QuestionDb(models.Model):

    Titile = models.CharField(max_length=100)

    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('java', 'Java'),
        ('cpp', 'C++'),
    )

    language_choice = models.CharField(
        max_length=100,
        choices=LANGUAGE_CHOICES
    )

    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    Difficulty_level = models.CharField(
        max_length=100,
        choices=DIFFICULTY_CHOICES
    )

    score = models.IntegerField()
    topic = models.CharField(max_length=100)
    notes = models.TextField()
    publishe_date = models.DateTimeField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    is_activate = models.BooleanField(default=True)

class SubmissionDb(models.Model):
    answer = models.TextField()
    question_id = models.IntegerField()
    owner = models.TextField()
    points = models.IntegerField()
    Submission_date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField()

