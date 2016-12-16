from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50) 
    content = models.TextField(max_length=400)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
