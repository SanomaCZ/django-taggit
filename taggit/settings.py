from django.conf import settings

TAGGIT_ENABLE_SPACE_SPLIT_IF_NOT_QUOTES = getattr(settings, 'TAGGIT_ENABLE_SPACE_SPLIT_IF_NOT_QUOTES', True)
