from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import TranslatorSerializer
from .models import Translator
from django.core.signals import request_finished
from analytics.mixins import ObjectViewMixin
from analytics.signals import object_viewed_signal


class TranslatorView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = TranslatorSerializer(data=request.data)

        if not serializer.is_valid():
            print("not valid")
            print(serializer.errors)
            return Response({"message": "not valid"}, status=400)
        print("valid")
        return Response({"message": "valid"}, status=200)

    def get(self, request):

        translators = Translator.objects.all()
        serializer = TranslatorSerializer(translators, many=True)
        object_viewed_signal.send(
            translators.first().__class__, instance=translators.first(), request=request)
        return Response(serializer.data)
