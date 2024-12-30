from rest_framework import serializers
from .models import Form, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'type', 'options', 'order']


class FormSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'is_active', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        form = Form.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(form=form, **question_data)
        return form
