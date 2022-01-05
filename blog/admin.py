from django.contrib import admin

# Register your models here.
from blog.models import Posts, Category

admin.site.register(Posts)
admin.site.register(Category)