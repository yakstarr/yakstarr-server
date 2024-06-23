from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DetailedDrug, DrugReview
from .serializers import DetailedDrugSerializer, DrugReviewSerializer
from django.db.models import Count

# 약 전체 목록 불러오기
class DetailedDrugListView(generics.ListAPIView):
    queryset = DetailedDrug.objects.all()
    serializer_class = DetailedDrugSerializer

# 약 이름으로 검색하기
class DetailedDrugSearchView(generics.ListAPIView):
    serializer_class = DetailedDrugSerializer

    def get_queryset(self):
        queryset = DetailedDrug.objects.all()
        drug_name = self.request.query_params.get('drug_name', None)
        if drug_name is not None:
            queryset = queryset.filter(drug_name__icontains=drug_name)
        return queryset

# 약 카테고리별 불러오기
class DetailedDrugCategoryView(generics.ListAPIView):
    serializer_class = DetailedDrugSerializer

    def get_queryset(self):
        queryset = DetailedDrug.objects.all()
        drug_category = self.request.query_params.get('drug_category', None)
        if drug_category:
            queryset = queryset.filter(drug_category__icontains=drug_category)
        return queryset

# 약 상세 불러오기 (약 하나 만)
class DetailedDrugDetailView(generics.RetrieveAPIView):
    queryset = DetailedDrug.objects.all()
    serializer_class = DetailedDrugSerializer

# 댓글 작성하기
class DrugReviewCreateView(generics.CreateAPIView):
    queryset = DrugReview.objects.all()
    serializer_class = DrugReviewSerializer

# 댓글 불러오기
class DrugReviewListView(generics.ListAPIView):
    serializer_class = DrugReviewSerializer

    def get_queryset(self):
        drug_id = self.kwargs.get('drug_id')
        if drug_id is not None:
            return DrugReview.objects.filter(drug_id=drug_id)
        return DrugReview.objects.none()

# 댓글 도움 되는 순으로 불러오기
class DrugReviewHelpfulListView(generics.ListAPIView):
    serializer_class = DrugReviewSerializer

    def get_queryset(self):
        drug_id = self.kwargs.get('drug_id')
        if drug_id is not None:
            return DrugReview.objects.filter(drug_id=drug_id).annotate(helpfulness=Count('likes')-Count('dislikes')).order_by('-helpfulness')
        return DrugReview.objects.none()

# 댓글 좋아요
class DrugReviewLikeView(generics.UpdateAPIView):
    queryset = DrugReview.objects.all()
    serializer_class = DrugReviewSerializer

    def patch(self, request, *args, **kwargs):
        review = self.get_object()
        review.likes += 1
        review.save()
        return Response({'likes': review.likes}, status=status.HTTP_200_OK)

# 댓글 싫어요
class DrugReviewDislikeView(generics.UpdateAPIView):
    queryset = DrugReview.objects.all()
    serializer_class = DrugReviewSerializer

    def patch(self, request, *args, **kwargs):
        review = self.get_object()
        review.dislikes += 1
        review.save()
        return Response({'dislikes': review.dislikes}, status=status.HTTP_200_OK)
    
class DrugReviewUpdateView(generics.UpdateAPIView):
    queryset = DrugReview.objects.all()
    serializer_class = DrugReviewSerializer

    def patch(self, request, *args, **kwargs):
        review = self.get_object()
        password = request.data.get('password')
        
        if password is not None and review.password == password:
            update_serializer = self.get_serializer(review, data=request.data, partial=True)
            update_serializer.is_valid(raise_exception=True)
            update_serializer.save()
            return Response(update_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid password.'}, status=status.HTTP_403_FORBIDDEN)

class DrugReviewDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        review = generics.get_object_or_404(DrugReview, pk=kwargs['pk'])
        password = request.data.get('password')

        if password is not None and review.password == password:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Invalid password.'}, status=status.HTTP_403_FORBIDDEN)