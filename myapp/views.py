from rest_framework import viewsets
from .models import User, Course, Score, Lesson, Quiz, Question
from .serializers import UserSerializer, CourseSerializer, ScoreSerializer, LessonSerializer, QuizSerializer, QuestionSerializer
import logging

logger = logging.getLogger(__name__)

from rest_framework import viewsets, status
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        logger.debug(f"Received POST request: {request.data}")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.debug(f"User created: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Bad Request: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
