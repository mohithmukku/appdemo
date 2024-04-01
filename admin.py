from django.contrib import admin
from .models import Blog
from .models import Contact
from .models import MarksForm
# from .models import AddBooks

# Register your models here.
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(MarksForm)