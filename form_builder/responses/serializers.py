from rest_framework import serializers
from .models import Response, Answer
from forms.models import Question

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer']


class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'form', 'submitted_at', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        response = Response.objects.create(**validated_data)
        for answer_data in answers_data:
            question = answer_data['question']
            Answer.objects.create(response=response, question=question, answer=answer_data['answer'])
        return response
