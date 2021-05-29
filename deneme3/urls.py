
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.views import APIView
from rest_framework.response import Response


class DenemeView(APIView):

    def post(self, request):
        print("requested to deneme view post method")
        return Response({"message": "merhaba"}, status=200)


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    url(r"^user/", include("User.urls")),
    url(r"^book/", include("Book.urls")),
    url(r"^deneme/$", DenemeView.as_view()),

]
