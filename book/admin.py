from django.contrib import admin
from book.models import author, books
from login.models import login
admin.site.register(books)
admin.site.register(author)
admin.site.register(login)

# Register your models here.
