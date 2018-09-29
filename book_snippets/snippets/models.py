from django.db import models
from extended_choices import Choices
from datetime import datetime

# Create your models here.
class Author(models.Model):
    name = models.fields.CharField(
        "Author's full name"
    )
    birth_year = models.fields.SmallIntegerField()
    death_year = models.fields.SmallIntegerField()

    def __str__(self):
        return self.name


class Source(models.Model):
    PUBLICATION_TYPES = Choices(
        ('BOOK', 1, 'book'),
    )

    title = models.fields.CharField()
    authors = models.ManyToManyField(Author)
    date_published = models.fields.DateField()
    type = models.PositiveSmallIntegerField(
        choices=PUBLICATION_TYPES,
        default=PUBLICATION_TYPES.BOOK
    )

    def __str__(self):
        if self.authors.count == 1:
            return ("%s by %s") % (self.title, self.author)

class Tag(models.Model):
    """
    Tags
    """
    code = models.fields.SlugField(primary_key=True)
    name = models.fields.CharField()
    description = models.fields.TextField()

    def __str__(self):
        return self.name

class Snippet(models.Model):
    snippet_text = models.fields.TextField()
    source = models.ForeignKey(Source)
    date_added = models.fields.DateField(default=datetime.now) # callable, so get correct datetime