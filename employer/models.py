from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.PositiveBigIntegerField(null=True)
    experience=models.PositiveBigIntegerField(default=0)


#python manage.py makemigrations :create query
#python manage.py migrate :stored in data base
# from employer.models import Jobs

# 1.orum query for creating a new job object:
# Jobs.objects.create(job_title_name="front end developer",company_name="info sys",location="kakkanad",salary="65000",experience="1")
# Jobs.objects.create(job_title_name="django developer",company_name="wipro",location="kakkanad",salary="35000",experience="3")
# Jobs.objects.create(job_title_name="software testing",company_name="tcs",location="kakkanad",salary="55000",experience="7")

#2.fetch all records from database
#qs=Jobs.object.all()

    def __str__(self):
        return self.job_title_name


#3.filter
# qs=Jobs.objects.filter(experience=1)
# qs

#qs=Jobs.objects.filter(experience__gt=1)


