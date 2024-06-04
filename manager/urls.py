from django.urls import path,include
from django.conf import settings

from django.conf.urls.static import static
from .views import Index, FormQuetions,FormQuiz
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('quetions',FormQuetions.as_view(),name='quetions'),
    path('quiz',FormQuiz.as_view(),name='quiz'),
]
