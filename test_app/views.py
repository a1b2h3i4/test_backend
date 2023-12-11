from http import HTTPStatus

from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def health_check(request):
    return HttpResponse("All Ok!Don't worry", status=200)
