from collections import OrderedDict
from rest_framework import serializers


class AlreadySubscribedCheck:
    from django.template.defaulttags import url

    from config import settings
    from user import serializers

    is_valid = False
    for allowed_url in settings.ALLOWED_URLS:
        if allowed_url in url:
            is_valid = True

    if not is_valid:
        raise serializers.ValidationError(
            'Использование стороннего ресурса недопустимо!'
        )