from django.contrib import admin

from .models import Category, Livro, Author

class AuthorAdmin(admin.ModelAdmin):
    ...

class CategoryAdmin(admin.ModelAdmin):
    ...

class LivroAdmin(admin.ModelAdmin):
    ...

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...