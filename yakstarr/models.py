from django.db import models


class DetailedDrug(models.Model):
    drug_image = models.ImageField(blank=True, upload_to='drug_images/')  # 약 사진
    drug_name = models.CharField(max_length=255)  # 약 이름
    drug_summary = models.CharField(max_length=255, blank=True, null=True)  # 약 간단한 설명
    drug_description = models.TextField(blank=True, null=True)  # 약 상세 설명
    drug_category = models.CharField(max_length=255, blank=True, null=True)  # 약 카테고리
    average_rating = models.FloatField(blank=True, null=True)  # 평균 별점

    def __str__(self):
        return self.drug_name


class DrugReview(models.Model):
    drug = models.ForeignKey(DetailedDrug, on_delete=models.CASCADE)  # FK 연관
    review_text = models.TextField()  # 약에 대한 평가
    nickname = models.CharField(max_length=255)  # 닉네임
    password = models.CharField(max_length=255)  # 비밀번호
    rating = models.IntegerField()  # 별점
    likes = models.IntegerField(default=0)  # 좋아요 수
    dislikes = models.IntegerField(default=0)  # 싫어요 수

    def __str__(self):
        return f'{self.nickname} - {self.drug.drug_name}'
