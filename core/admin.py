from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'title',
        'is_correct'
    ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['type', 'title', 'quiz',]
    list_display = [ 'id','title', 'type', 'quiz']
    inlines = [AnswerInlineModel]