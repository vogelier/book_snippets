from django.db import models
from django.utils.translation import ugettext_lazy as _

from extended_choices import Choices
from datetime import datetime


# Create your models here.
class Author(models.Model):
    name = models.fields.CharField(
        _('Author full name'),
        max_length=255
    )
    birth_year = models.fields.SmallIntegerField()
    death_year = models.fields.SmallIntegerField()

    def __str__(self):
        return self.name


class Source(models.Model):
    # TODO - i18n support here
    PUBLICATION_TYPES = Choices(
        ('BOOK', 1, 'book'),
    )

    title = models.fields.CharField(
        max_length=255
    )
    authors = models.ManyToManyField(Author)
    date_published = models.fields.DateField()
    type = models.PositiveSmallIntegerField(
        choices=PUBLICATION_TYPES,
        default=PUBLICATION_TYPES.BOOK
    )

    def __str__(self):
        if self.authors.count == 1:
            return _("%s by %s") % (self.title, self.authors.objects.first())


class Tag(models.Model):
    """
    Tags
    """
    code = models.fields.SlugField(primary_key=True)
    name = models.fields.CharField(max_length=255)
    description = models.fields.TextField()

    def __str__(self):
        return self.name


class Snippet(models.Model):
    snippet_text = models.fields.TextField()
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    date_added = models.fields.DateField(default=datetime.now)  # callable, so get correct datetime
    tags = models.ManyToManyField(Tag)
