from rest_framework.serializers import ModelSerializer
from courses.models import Category, Course, Lesson


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url

        return rep

class CourseSerializer(ItemSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'description', 'image', 'active', 'category', 'created_date']


class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'created_date', 'image']


class LessonDetailsSerializer(LessonSerializer):
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'updated_date', 'tags']