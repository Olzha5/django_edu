from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, ScoreViewSet, LessonViewSet, QuizViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
