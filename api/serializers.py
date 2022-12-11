from rest_framework import serializers
from django.contrib.auth.models import User, update_last_login
from core.models import *
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta: 
        model = Question
        fields = ['id', 'title', 'type', 'answers']

# class SubmitAnswerSerializer(serializers.Serializer):
#     def validate(self, data):
#         if data['type'] == 0:
#             raise serializers.ValidationError("finish must occur after start")
#         return data

#     question = serializers.UUIDField()
#     type = serializers.IntegerField()
#     answer = serializers.UUIDField(required=False)
#     answers = serializers.ListField(required=False)

class TestiongSerializer(serializers.Serializer):
    quiz = serializers.ListField()
    # class Meta: 
    #     model = Question
    #     fields = '__all__'
    def get_quiz(self, instance):
        print(instance, '-----------------')

class SubmitAnswersSerializer(serializers.Serializer):
    data = serializers.ListField()

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        print(email)
        password = data.get("password", None)
        print(password)
        user = authenticate(email=email, password=password,)
        print(user)
        if user is None:
            raise serializers.ValidationError(
                'Invalid Credentials'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Invalid Credentials'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }