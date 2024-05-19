from rest_framework.serializers import ModelSerializer, SerializerMethodField

from rest_framework import serializers
from .models import FAQ, Requirements


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        read_only_fields = ['id']


class FAQGetSerializer(ModelSerializer):
    faq_question = SerializerMethodField()
    faq_answer = SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ('id', 'faq_question', 'faq_answer')

    def get_faq_question(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.FAQ_name_en
        return obj.FAQ_name_uz

    def get_faq_answer(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.answer_en
        return obj.answer_uz


class RequirementsSerializer(ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'


class RequirementsGetSerializer(ModelSerializer):
    requirements_title = SerializerMethodField()
    requirements_part = SerializerMethodField()
    requirements_description = SerializerMethodField()

    class Meta:
        model = Requirements
        fields = ('id', 'requirements_title', 'requirements_part', 'requirements_description')

    def get_requirements_title(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.requirements_title_en
        return obj.requirements_title_uz

    def get_requirements_part(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.requirements_parts_en
        return obj.requirements_parts_uz

    def get_requirements_description(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.requirements_description_en
        return obj.requirements_description_uz


class UserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=500)
    subject = serializers.CharField(max_length=100)