
from rest_framework import serializers
from Repository.models import QuestionDb


class QuestionSerializer(serializers.Serializer):
    Titile = serializers.CharField(max_length=100)

    language_choice = serializers.ChoiceField(
        choices=QuestionDb.LANGUAGE_CHOICES
    )

    Difficulty_level = serializers.ChoiceField(
        choices=QuestionDb.DIFFICULTY_CHOICES
    )

    topic = serializers.CharField(max_length=100)
    score = serializers.IntegerField()
    publishe_date = serializers.DateTimeField(read_only=True)
    notes = serializers.CharField()
    sample_input = serializers.CharField()
    sample_output = serializers.CharField()
    is_activate = serializers.BooleanField(default=True)
class SubmissionSerializer(serializers.Serializer):
    answer = serializers.CharField()
    question_id = serializers.IntegerField()
    points = serializers.IntegerField(read_only=True)
    remarks = serializers.CharField(read_only=True)
    Submission_date = serializers.DateTimeField(read_only=True)
    

    def validate(self,validated_data):

        question_id = validated_data.get("question_id")

        if not QuestionDb.objects.filter(id=question_id).exists():

            raise serializers.ValidationError("Question does not exist")
        return 