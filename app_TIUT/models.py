from django.db import models


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

