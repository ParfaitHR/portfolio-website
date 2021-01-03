from django.db import models

# Create your models here.
class Job(models.Model):

    STATUS = (
        ('Accepting CVs', 'Accepting CVs'),
        ('Interviewing', 'Interviewing'),
        ('Vacancy Filled', 'Vacancy Filled'),
    )

    job_title = models.CharField(max_length=30, null=True)
    company_name = models.CharField(max_length=30, null=True)
    salary = models.CharField(max_length=30, null=True)
    vacancies = models.IntegerField(null=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (self.job_title + ' | ' + self.company_name)
