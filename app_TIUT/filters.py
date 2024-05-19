
import django_filters
from .models import Paper, Sphere, Requirements, Publication


class PaperFilter(django_filters.FilterSet):
    paper_title = django_filters.CharFilter(field_name='paper_title_uz', lookup_expr='icontains')
    paper_author = django_filters.CharFilter(field_name='paper_author_uz', lookup_expr='icontains')
    paper_keywords = django_filters.CharFilter(field_name='paper_keywords_uz', lookup_expr='icontains')
    paper_sphere = django_filters.ModelChoiceFilter(queryset=Sphere.objects.all())

    class Meta:
        model = Paper
        fields = ['paper_title', 'paper_author', 'paper_keywords', 'paper_sphere']


class RequirementsFilter(django_filters.FilterSet):
    requirements_parts_uz = django_filters.CharFilter(lookup_expr='icontains')
    requirements_parts_en = django_filters.CharFilter(lookup_expr='icontains')
    requirements_title_uz = django_filters.CharFilter(lookup_expr='icontains')
    requirements_title_en = django_filters.CharFilter(lookup_expr='icontains')
    requirements_description_uz = django_filters.CharFilter(lookup_expr='icontains')
    requirements_description_en = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Requirements
        fields = [
            'requirements_parts_uz',
            'requirements_parts_en',
            'requirements_title_uz',
            'requirements_title_en',
            'requirements_description_uz',
            'requirements_description_en',
        ]


class PublicationFilter(django_filters.FilterSet):
    pub_name_uz = django_filters.CharFilter(lookup_expr='icontains')
    pub_name_en = django_filters.CharFilter(lookup_expr='icontains')
    pub_description_uz = django_filters.CharFilter(lookup_expr='icontains')
    pub_description_en = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Publication
        fields = [
            'pub_name_uz',
            'pub_name_en',
            'pub_description_uz',
            'pub_description_en',
            'pub_sphere',
        ]
