from django.http import HttpResponse
from rest_framework import viewsets, generics, status
from courses.models import Category, Course, Lesson
from rest_framework.response import Response
from courses import serializers
from rest_framework.decorators import action
from courses.pagination import CoursePagination


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class CategoryViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = CoursePagination

    def get_queryset(self):
        queryset = self.queryset

        if self.action.__eq__('list'):
            q = self.request.query_params.get('q')
            cate_id = self.request.query_params.get('category_id')
            if q:
                queryset = Course.objects.filter(subject__icontains=q)
            if cate_id:
                queryset = Course.objects.filter(category_id=cate_id)

        return queryset

    @action(detail=True, methods=['GET'], url_path='lessons')
    def get_lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)

        q = request.query_params.get('q')
        if q:
            lessons = lessons.filter(subject__icontains=q)

        return Response(serializers.LessonSerializer(lessons, many=True).data, status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = serializers.LessonDetailsSerializer