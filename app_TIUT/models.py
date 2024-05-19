from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings




class FAQ(models.Model):
    FAQ_name_uz = models.CharField(max_length=100)
    FAQ_name_en = models.CharField(max_length=100)
    answer_uz = models.TextField()
    answer_en = models.TextField()

    def __str__(self):
        return self.FAQ_name_uz

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        db_table = 'FAQ'


class Requirements(models.Model):
    requirements_parts_uz = models.CharField(max_length=100)
    requirements_parts_en = models.CharField(max_length=100)
    requirements_title_uz = models.TextField()
    requirements_title_en = models.TextField()
    requirements_description_uz = models.TextField()
    requirements_description_en = models.TextField()

    def __str__(self):
        return self.requirements_parts_uz

    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'
        db_table = 'Requirements'


class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'User'
        db_table = 'userinfo'


class Sphere(models.Model):
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Sphere'
        db_table = 'sphere'


class Publication(models.Model):
    '''Bitta Pulicationda kop fanlardan malumotlar bolganligi sababli
    Sphere bilan Many to Many boglanish boladi'''
    pub_name_uz = models.CharField(max_length=100)
    pub_name_en = models.CharField(max_length=100)
    pub_description_uz = models.TextField()
    pub_description_en = models.TextField()
    pub_file_uz = models.FileField(upload_to='publications/', null=True, blank=True)
    pub_file_en = models.FileField(upload_to='publications/', null=True, blank=True)
    image = models.ImageField(upload_to='publications/')
    views_count = models.IntegerField(default=0)
    pub_sphere = models.ManyToManyField(Sphere, related_name='publications')

    def __str__(self):
        return self.pub_name_uz

    class Meta:
        verbose_name = 'Publication'
        db_table = 'publication'


class Paper(models.Model):
    '''Bitta paper faqaat bitta fan boyicha boladi shuning uchun
    Paper bilan Sphere FK boglanish boladi'''
    paper_title_uz = models.CharField(max_length=100)
    paper_title_en = models.CharField(max_length=100)
    paper_text_uz = models.TextField()
    paper_text_en = models.TextField()
    paper_file_uz = models.FileField(upload_to='papers/', null=True, blank=True)
    paper_file_en = models.FileField(upload_to='papers/', null=True, blank=True)
    paper_keywords_uz = models.CharField(max_length=100)
    paper_keywords_en = models.CharField(max_length=100)
    paper_sphere = models.ForeignKey(Sphere, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)
    reviews = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='paper_reviews')

    def __str__(self):
        return self.paper_title_uz

    class Meta:
        verbose_name = 'Paper'
        db_table = 'paper'


class Review(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='paper_reviews')  # Changed related_name
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    review_file = models.FileField(upload_to='reviews/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.reviewer} for {self.paper}'

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        unique_together = (('paper', 'reviewer'),)





