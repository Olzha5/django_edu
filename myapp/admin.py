from django.contrib import admin
from .models import Lesson, User, Question, Quiz, Course,Score

class LessonAdmin(admin.ModelAdmin):
    list_display = ('video', 'documents', 'text')
    list_filter = ('video', 'documents', 'text')
    search_fields = ('video', 'documents', 'text')
    ordering = ['video']
    readonly_fields = ('video', 'documents', 'text')
    fieldsets = (
        (None, {
            'fields': ('video', 'documents', 'text')
        }),
    )
admin.site.register(Lesson, LessonAdmin)

    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_of_birth', 'status', 'int_courses', 'courses')
    list_filter = ('username', 'date_of_birth', 'status', 'int_courses', 'courses')
    search_fields = ('username', 'date_of_birth', 'status', 'int_courses', 'courses')
    ordering = ['username']
    readonly_fields = ('username', 'date_of_birth', 'status', 'int_courses', 'courses')
    
admin.site.register(User, UserAdmin)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'information', 'author', 'display_quizzes', 'display_lessons', 'image')

    def display_quizzes(self, obj):
        return ", ".join([quiz.title for quiz in obj.quizzes.all()])
    display_quizzes.short_description = 'Quizzes'

    def display_lessons(self, obj):
        return ", ".join([lesson.text for lesson in obj.lessons.all()])
    display_lessons.short_description = 'Lessons'

admin.site.register(Course, CourseAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_questions')

    def display_questions(self, obj):
        return ", ".join([question.text for question in obj.questions.all()])
    display_questions.short_description = 'Questions'

admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'options', 'right_option')
    list_filter = ('text', 'options', 'right_option')
    search_fields = ('text', 'options', 'right_option')
    ordering = ['text']
    readonly_fields = ('text', 'options', 'right_option')
    fieldsets = (
        (None, {
            'fields': ('text', 'options', 'right_option')
        }),
    )
    filter_horizontal = ()
    raw_id_fields = ()

admin.site.register(Question, QuestionAdmin)
    


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'score')
    list_filter = ('user', 'course', 'score')
    search_fields = ('user', 'course', 'score')
    readonly_fields = ('user', 'course', 'score')
    fieldsets = (
        (None, {
            'fields': ('user', 'course', 'score')
        }),
    )
    filter_horizontal = ()
    raw_id_fields = ()
admin.site.register(Score, ScoreAdmin)
