from django.contrib import admin

from .models import Category, Livro, Author, Emprestimo

class EmprestimoAdmin(admin.ModelAdmin):
    ...

class AuthorAdmin(admin.ModelAdmin):
    ...

class CategoryAdmin(admin.ModelAdmin):
    ...

class LivroAdmin(admin.ModelAdmin):
    ...

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    ...

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...