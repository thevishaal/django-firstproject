from django.contrib import admin
from .models import Question

admin.site.site_header = "Polls Admin"
admin.site.index_title = "Amazing Title"
# Register your models here.
admin.site.register(Question)