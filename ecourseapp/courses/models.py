from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField(null=True)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True, blank=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ItemBase(BaseModel):
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True


class Course(ItemBase):
    subject = models.CharField(max_length=50)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


class Lesson(ItemBase):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = CloudinaryField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Like(Interaction):

    class Meta:
        unique_together = ('user', 'lesson')


class Comment(Interaction):
    content = models.CharField(max_length=255)