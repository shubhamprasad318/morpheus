from rest_framework.decorators import api_view
from rest_framework.response import Response
from forms.models import Form, Question
from responses.models import Answer

@api_view(['GET'])
def form_analytics(request, form_id):
    try:
        form = Form.objects.get(id=form_id)
        analytics = {
            'response_count': form.responses.count(),
            'questions': []
        }

        for question in form.questions.all():
            question_data = {'id': question.id, 'type': question.type, 'analytics': {}}
            answers = Answer.objects.filter(question=question)

            if question.type == 'Text':
                word_counts = {}
                for answer in answers:
                    for word in answer.answer.split():
                        if len(word) >= 5:
                            word_counts[word] = word_counts.get(word, 0) + 1
                sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
                question_data['analytics']['common_words'] = [{'word': word, 'count': count} for word, count in sorted_words]

            elif question.type in ['Dropdown', 'Checkbox']:
                option_counts = {}
                for answer in answers:
                    options = answer.answer if question.type == 'Checkbox' else [answer.answer]
                    for option in options:
                        option_counts[option] = option_counts.get(option, 0) + 1
                sorted_options = sorted(option_counts.items(), key=lambda x: x[1], reverse=True)[:5]
                question_data['analytics']['top_options'] = [{'option': opt, 'count': cnt} for opt, cnt in sorted_options]

            analytics['questions'].append(question_data)

        return Response(analytics)

    except Form.DoesNotExist:
        return Response({'error': 'Form not found'}, status=404)
