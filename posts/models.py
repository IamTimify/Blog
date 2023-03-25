from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator


User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = models.ImageField()
    profile_picture = CloudinaryField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])


    def __str__(self):
        return f'{self.user.username}'

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    # thumbnail = models.ImageField()
    thumbnail = CloudinaryField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])


    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # thumbnail = models.ImageField()
    thumbnail = CloudinaryField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post", kwargs={"slug": str(self.slug)})


class Contact(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11, blank=False,null=False)