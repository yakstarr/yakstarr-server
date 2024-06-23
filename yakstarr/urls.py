from django.urls import path
from .views import (
    DetailedDrugListView, 
    DetailedDrugSearchView, 
    DetailedDrugCategoryView, 
    DetailedDrugDetailView, 
    DrugReviewCreateView,
    DrugReviewListView, 
    DrugReviewHelpfulListView,
    DrugReviewLikeView,
    DrugReviewDislikeView,
)

urlpatterns = [
    path('drugs/', DetailedDrugListView.as_view(), name='drug-list'),
    path('drugs/search/', DetailedDrugSearchView.as_view(), name='drug-search'),
    path('drugs/category/', DetailedDrugCategoryView.as_view(), name='drug-category'),
    path('drugs/<int:pk>/', DetailedDrugDetailView.as_view(), name='drug-detail'),
    path('drugs/reviews/', DrugReviewCreateView.as_view(), name='drug-review-create'),
    path('drugs/reviews/<int:drug_id>/', DrugReviewListView.as_view(), name='drug-review-list'),
    path('drugs/reviews/helpful/<int:drug_id>/', DrugReviewHelpfulListView.as_view(), name='helpful-drug-review-list'),
    path('drugs/reviews/like/<int:pk>/', DrugReviewLikeView.as_view(), name='drug-review-like'),
    path('drugs/reviews/dislike/<int:pk>/', DrugReviewDislikeView.as_view(), name='drug-review-dislike'),
   ]
