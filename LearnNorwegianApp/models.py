from django.db import models
from django.db.models import Q


class vocabularyQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(word_in_polish__icontains=query) | Q(word_in_norwegian__icontains=query)
        return self.filter(lookups)


class vocabularyManager(models.Manager):
    def get_queryset(self):
        return vocabularyQuerySet(self.model, using=self.db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class vocabulary(models.Model):
    id = models.IntegerField(primary_key=True)
    word_in_norwegian = models.CharField(max_length=70)
    word_in_polish = models.CharField(max_length=70)
    word_in_english = models.CharField(max_length=70)
    category = models.CharField(max_length=70, blank=True)

    objects=vocabularyManager()

    def __str__(self):
        return self.word_in_norwegian + " " + self.word_in_polish


class uregelrette_verb(models.Model):
    id = models.IntegerField(primary_key=True)
    infinitiv = models.CharField(max_length=50)
    presens = models.CharField(max_length=50)
    preteritum = models.CharField(max_length=50)
    presens_perfektum = models.CharField(max_length=50)
    polski = models.CharField(max_length=50)

    def __str__(self):
        return self.infinitiv + ' ' + self.polski
