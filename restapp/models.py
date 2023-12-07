from django.db import models


class Journalist(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(
        Journalist, on_delete=models.CASCADE, related_name="articles"
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    main_text = models.TextField()
    published_time = models.DateField()
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
