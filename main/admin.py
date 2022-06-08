from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Actor),
admin.site.register(Movie),
admin.site.register(Category),
admin.site.register(Director),
admin.site.register(Genre),
admin.site.register(Review)
