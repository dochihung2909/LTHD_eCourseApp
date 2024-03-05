from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from courses.models import Category, Course


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class MyCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'active']
    readonly_fields = ['view_image']

    def view_image(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=obj.image.name)
            )


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'category', 'active']
    search_fields = ['id', 'subject']
    readonly_fields = ['view_image']
    form = CourseForm

    def view_image(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=obj.image.name)
            )


# Register your models here.
admin.site.register(Category, MyCategoryAdmin)
admin.site.register(Course, MyCourseAdmin)