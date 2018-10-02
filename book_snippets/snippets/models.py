from django.db import models
from django.utils.translation import ugettext_lazy as _

from extended_choices import Choices
from datetime import datetime
from model_utils.models import StatusModel

# TODO - look at url model mixin or is it same as slug mixin?
# TODO - do we need a mixin for model creation/update
# Create your models here.

class Tag(models.Model):
    """
    Tags
    """
    code = models.fields.SlugField(primary_key=True)
    name = models.fields.CharField(max_length=255)
    description = models.fields.TextField(blank=True)

    def __str__(self):
        return self.code


class Author(models.Model):
    given_name = models.fields.CharField(
        max_length=255
    )
    middle_name = models.fields.CharField(
        max_length=255,
        blank=True,
        default=''
    )
    family_name = models.fields.CharField(
        max_length=255
    )
    birth_year = models.fields.SmallIntegerField(blank=True, default=0)
    death_year = models.fields.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return ("%s %s") % (self.given_name, self.family_name)


class Source(models.Model):
    # TODO - i18n support here
    PUBLICATION_TYPES = Choices(
        ('BOOK', 1, 'book'),
    )

    title = models.fields.CharField(
        max_length=255
    )
    authors = models.ManyToManyField(Author, related_name='all_work')
    date_published = models.fields.DateField(null=True)
    type = models.PositiveSmallIntegerField(
        choices=PUBLICATION_TYPES,
        default=PUBLICATION_TYPES.BOOK
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class ReadingStatus(StatusModel, models.Model):
    STATUS = Choices(
        ('NOW_READING', 'now reading', 'Now reading'),
        ('READ', 'read', 'Read'),
        ('STALLED', 'stalled', 'Stalled'),
        ('TO_READ', 'to read', 'To Read')
    )
    source = models.ForeignKey(Source, on_delete=models.CASCADE)


class KnowledgeTransferStatus(StatusModel, models.Model):
    STATUS = Choices(
        ('TRANSFER_DONE', 'transferred', 'Transferred'),
        ('IN_PROGRESS', 'in progress', 'In Progress'),
        ('NOT_STARTED', 'not started', 'Not Started'),
        ('STALLED', 'stalled', 'Stalled'),
    )
    source = models.ForeignKey(Source, on_delete=models.CASCADE)


class Snippet(models.Model):
    LENGTH_LIMIT = 30
    text = models.fields.TextField()
    source = models.ForeignKey(
        Source,
        on_delete=models.SET_NULL,
        null=True
    )
    date_added = models.fields.DateField(default=datetime.now)  # callable, so get correct datetime
    tags = models.ManyToManyField(Tag, related_name='tagged_snippets')

    def __str__(self):
        if not len(self.text.__str__()) > self.LENGTH_LIMIT:
            return self.text.__str__()
        return self.text.__str__()[:self.LENGTH_LIMIT] + '...'


class IndexEntry(models.Model):
    page = models.IntegerField()
    topic = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        null=True
    )
    note = models.TextField(blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='indexes')
