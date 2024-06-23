from rest_framework import serializers
from .models import DetailedDrug, DrugReview
from django.db.models import Avg

class DetailedDrugSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = DetailedDrug
        fields = '__all__'

    def get_review_count(self, obj):
        return DrugReview.objects.filter(drug=obj).count()

    def get_average_rating(self, obj):
        return DrugReview.objects.filter(drug=obj).aggregate(Avg('rating'))['rating__avg']

class DrugReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugReview
        fields = '__all__'
