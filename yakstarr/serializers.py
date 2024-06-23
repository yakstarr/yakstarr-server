from rest_framework import serializers
from .models import DetailedDrug, DrugReview

class DetailedDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedDrug
        fields = '__all__'

class DrugReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugReview
        fields = '__all__'
