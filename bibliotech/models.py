from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=65)

    def __str__ (self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__ (self):
        return self.name
    
class Livro(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='bibliotech/covers/%Y/%m/%d/')
    quantidade = models.CharField(max_length=15)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True
    )
    """
    user = models.ForenKey(
        User, on_delete=models.SET_NULL, null=True)
    """

    def __str__ (self):
        return self.title
    
"""
class Emprestimo(models.Model):
    user = models.ForenKey(
        User, on_delete=models.SET_NULL, null=True)
    data_retirada = models.DateTime()
"""