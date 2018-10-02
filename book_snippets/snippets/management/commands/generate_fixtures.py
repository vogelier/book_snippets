from django.core.management.base import BaseCommand, CommandError

from snippets.models import *


class Command(BaseCommand):
    help = 'Generates some dummy data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Creating dummy data for our snippets app')
        # Kill everything first
        Author.objects.all().delete()
        Source.objects.all().delete()
        Tag.objects.all().delete()
        Snippet.objects.all().delete()

        # Books and authors
        self.stdout.write('Creating some books and authors...')
        darwin = Author(
            given_name='Charles',
            family_name='Darwin',
            birth_year=1809,
            death_year=1882
        )
        darwin.save()
        on_origin = Source(
            title='On the origin of species',
        )
        on_origin.save()
        on_origin.authors.add(darwin)

        kurt_andereson = Author(
            given_name='Kurt',
            family_name='Andereson',
            birth_year=1954
        )
        kurt_andereson.save()
        fantasyland = Source(
            title='Fantasyland: How America Went Haywire: A 500-Year History',
            date_published='2017-10-05',
        )
        fantasyland.save()
        fantasyland.authors.add(kurt_andereson)
        ReadingStatus(
            source=fantasyland,
            status=ReadingStatus.STATUS.READ).save()
        KnowledgeTransferStatus(
            source=fantasyland,
            status=KnowledgeTransferStatus.STATUS.NOT_STARTED
        ).save()

        # Tags
        self.stdout.write('Creating some tags...')
        history_tag = Tag(code='history', name='History')
        history_tag.save()
        biology_tag = Tag(code='bio', name='Biology')
        biology_tag.save()
        evo_biology_tag = Tag(code='evo-bio', name='Evolutionary Biology')
        evo_biology_tag.save()

        # Tag a book
        fantasyland.tags.add(history_tag)
        on_origin.tags.add(biology_tag, evo_biology_tag)