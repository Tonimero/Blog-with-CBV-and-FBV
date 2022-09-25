from django.db import models
from django.urls import reverse

# Create your models here.

class CategoryPage(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField( null=False, blank=False)
    
    def __str__(self) :
        return self.name

class Post(models.Model):
    categories = models.ForeignKey(CategoryPage, on_delete=models.CASCADE, related_name='categories', default="Select a category")
    title = models.CharField(max_length=300)
    info = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField()
    image = models.FileField(upload_to='static/blog_post_image/')
    published_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) :
        return self.title
    
    class Meta:
        ordering = ['-published_at']
        
    def get_absolute_url(self):
        return reverse("detailPage", kwargs={"slug": self.slug})
    