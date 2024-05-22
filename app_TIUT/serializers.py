from rest_framework.serializers import ModelSerializer, SerializerMethodField

from rest_framework import serializers

from users.models import CustomUser
from .models import (FAQ,
                     Requirements,
                     Sphere,
                     Publication,
                     Paper,
                     Review,
                     UserInfo,

                     )


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


class SphereSerializer(ModelSerializer):
    class Meta:
        model = Sphere
        fields = '__all__'


class SphereGetSerializer(ModelSerializer):
    sphere_name = SerializerMethodField(method_name='get_sphere_name', read_only=True)

    class Meta:
        model = Sphere
        fields = ('id', 'sphere_name')
        read_only_fields = ['id']

    def get_sphere_name(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.name_en
        return obj.name_uz


class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ['id', 'views_count']


class PublicationGetSerializer(ModelSerializer):
    publication_name = SerializerMethodField(method_name='get_publication_name', read_only=True)
    publication_description = SerializerMethodField(method_name='get_publication_description', read_only=True)
    publication_file = SerializerMethodField(method_name='get_publication_file', read_only=True)

    class Meta:
        model = Publication
        fields = ('id', 'publication_name', 'publication_description', 'publication_file')
        read_only_fields = ['id']

    def get_publication_name(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.pub_name_en
        return obj.pub_name_uz

    def get_publication_description(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.pub_description_en
        return obj.pub_description_uz

    def get_publication_file(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        file_field = obj.pub_file_en if lang == 'en' else obj.pub_file_uz
        if file_field:
            return file_field.url
        return None


class PaperSerializer(ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'
        read_only_fields = ['id', "views_count"]


class PaperGetSerializer(ModelSerializer):
    paper_title = SerializerMethodField(method_name='get_paper_name', read_only=True)
    paper_text = SerializerMethodField(method_name='get_paper_description', read_only=True)
    paper_file = SerializerMethodField(method_name='get_paper_file', read_only=True)
    paper_keywords = SerializerMethodField(method_name='get_paper_keywords', read_only=True)
    paper_author = SerializerMethodField(method_name='get_paper_author', read_only=True)

    class Meta:
        model = Paper
        fields = ('id', 'paper_title', 'paper_text', 'paper_keywords', 'paper_file', 'paper_author')
        read_only_fields = ['id']

    def get_paper_name(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.paper_title_en
        return obj.paper_title_uz

    def get_paper_description(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.paper_text_en
        return obj.paper_text_uz

    def get_paper_file(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        file = obj.paper_file_en if lang == 'en' else obj.paper_file_uz
        return file.url if file else None

    def get_paper_keywords(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.paper_keywords_en
        return obj.paper_keywords_uz

    def get_paper_author(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.paper_author_en
        return obj.paper_author_uz


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        if not self.context['request'].user.is_reviewer:
            raise serializers.ValidationError('Only reviewers can add reviews.')
        return data


# serializers.py

class ReviewPageSerializer(ModelSerializer):
    reviewer_name = serializers.CharField(source=CustomUser.username, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class PaperDetailSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Paper
        fields = '__all__'


class UserInformationSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
