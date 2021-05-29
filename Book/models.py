from django.db import models


class Translator(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, null=True)
    added_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="author")
    translator = models.ForeignKey(
        Translator, on_delete=models.CASCADE, related_name="translator", null=True)
    nick_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name}-{self.author.firstname} {self.author.lastname}"
