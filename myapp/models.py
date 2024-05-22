from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default="ccd")
    int_courses = models.IntegerField(default=0)
    courses = models.CharField(max_length=300, default="rfrf")
    

class Course(models.Model):
    name = models.CharField(max_length=255)
    information = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authored_courses')
    quizzes = models.ManyToManyField('Quiz', related_name='courses')
    lessons = models.ManyToManyField('Lesson', related_name='courses')
    def __str__(self):
        return self.name

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return self.user
class Lesson(models.Model):
    video = models.URLField(blank=True, null=True)
    documents = models.FileField(upload_to='documents/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.text
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField('Question', related_name='quizzes')
    def __str__(self):
        return self.title
    
class Question(models.Model):
    text = models.TextField()
    options = models.JSONField()  # A list of options
    right_option = models.IntegerField()  # Index of the correct option
    def __str__(self):
        return self.text 