from django.urls import path
from .views import *

urlpatterns = [
    path('auth/register/', RegisterAPI.as_view(), name='auth_register'),
    path('auth/login/', LoginAPI.as_view(), name='auth_login'),
    path('quizzes/<uuid:quiz_id>/', QuizQuestion.as_view(), name='quiz_questions'),
    path('quizzes/', Quiz.as_view(), name='quiz'),
]