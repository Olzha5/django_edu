from django.contrib import admin
from .models import Lesson, User, Question, Quiz, Course,Score

admin.site.register(Lesson)
admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Course)
admin.site.register(Score)
