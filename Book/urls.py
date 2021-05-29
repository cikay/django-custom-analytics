from django.conf.urls import url
from .views import TranslatorView


urlpatterns = [
    url(r"^translator/create/$", TranslatorView.as_view()),
    url(r"^translators/$", TranslatorView.as_view()),
]
