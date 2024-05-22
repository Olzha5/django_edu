from rest_framework import serializers
from .models import User, Course, Score, Lesson, Quiz, Question
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_of_birth', 'status', 'int_courses', 'courses']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            date_of_birth=validated_data.get('date_of_birth'),
            status=validated_data.get('status', 'ccd'),
            int_courses=validated_data.get('int_courses', 0),
            courses=validated_data.get('courses', 'rfrf'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'information', 'author', 'quizzes', 'lessons']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'user', 'course', 'score']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'video', 'documents', 'text']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'questions']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'options', 'right_option']
