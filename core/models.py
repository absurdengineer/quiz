from django.db import models
import uuid
from .enums import QUESTION_TYPE

# Base Model Defintion
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Quiz Model Definition
class Quiz(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Quizzes'

# Question Model Definition
class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, related_name='quiz', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.IntegerField(choices=QUESTION_TYPE, default=0, verbose_name="Type of Question")
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return 'Question: {}'.format(self.title)

    def get_answers(self):
        answers = Answer.objects.filter(question_id = self, is_correct=True)
        answer_list = []
        for answer in answers:
            answer_list.append(str(answer.id))
        return answer_list

# Answer Model Definition
class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title