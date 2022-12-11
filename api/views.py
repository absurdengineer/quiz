from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from core.models import *
from rest_framework import status

class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class QuizQuestion(APIView):

    def get(self, request, **kwargs):
        questions = Question.objects.filter(quiz=kwargs['quiz_id'], is_published=True)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, quiz_id):
        data = request.data
        score = 0
        if data:
            serializer = TestiongSerializer(data=data)
            if serializer.is_valid():
                if data['quiz']:
                    for question in data['quiz']:
                        if question['type'] == '0':
                            answer = Answer.objects.filter(question_id=question['question'], id = question['answer'], is_correct=True)
                            if answer:
                                score += 1
                        elif question['type'] == '1':
                            answers = Question.get_answers(question['question']) 
                            answers.sort()
                            question['answers'].sort()
                            if question['answers'] == answers:
                                score+=1
                else:
                    return Response({
                        'status': False,
                        'message': 'liiiiiii',
                    })
            else:
                return Response({
                    'status': False,
                    'message': 'serializer',
                })
            return Response({'status': status.HTTP_200_OK, 'score': score})
        else:   
            return Response({
                'status': False,
                'message': 'Plese input valid data.',
            })

class RegisterAPI(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if User.objects.filter(email=data['email']).exists():
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':"email must be unique",
            })
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            'message':"user created.",
        })

class LoginAPI(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)