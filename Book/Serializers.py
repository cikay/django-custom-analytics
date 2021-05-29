from rest_framework import serializers

from .models import Translator

class TranslatorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Translator
        fields = (
            "firstname",
            "lastname",
            "nick_name"
        )