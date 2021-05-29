from django.conf.urls import url
from .views import UserView

urlpatterns = [
    url(r"^create/$", UserView.as_view())
]