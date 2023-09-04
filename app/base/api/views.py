from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from parsers.api_parser.alif import Alif as Alf


class Test(APIView):
    """
    Test View
    """

    def get(self, request):
        return HttpResponse('Hello test')


class Alif(APIView):
    def get(self, request):
        alif = Alf()
        result = alif.parse_rates()

        return Response(result)

