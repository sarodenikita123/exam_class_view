from django.db import models


class HallTicket(models.Model):
    candidate_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    exam_name = models.CharField(max_length=20)
    center = models.CharField(max_length=20)
    date_of_exam = models.DateField()
    time = models.TimeField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
