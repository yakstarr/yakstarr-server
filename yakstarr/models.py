from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DetailedDrug(models.Model):
    drug_image = models.ImageField(blank=True, upload_to='drug_images/')
    drug_name = models.CharField(max_length=255, blank=False)
    drug_summary = models.CharField(max_length=255, blank=True, null=True)
    drug_element = models.CharField(max_length=255, blank=True, null=True)
    drug_company = models.CharField(max_length=255, blank=True, null=True)
    drug_effect = models.CharField(max_length=255, blank=True, null=True)
    drug_recipe = models.CharField(max_length=255, blank=True, null=True)
    drug_method = models.CharField(max_length=255, blank=True, null=True)
    drug_warning = models.CharField(max_length=255, blank=True, null=True)
    drug_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.drug_name

class DrugReview(models.Model):
    drug = models.ForeignKey(DetailedDrug, on_delete=models.CASCADE)
    review_text = models.TextField()
    nickname = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nickname} - {self.drug.drug_name}'
