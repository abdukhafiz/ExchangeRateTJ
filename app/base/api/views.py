from datetime import datetime

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from parsers.api.alif import Alif as AlifBank
from parsers.xml.nbt import Nbt as NBT


class Test(APIView):
    """
    Test View
    """

    def get(self, request):
        return HttpResponse(datetime.today().strftime('%Y-%m-%d'))


class Alif(APIView):
    def get(self, request):
        alif = AlifBank()
        result = alif.parse_rates()

        return Response(result)


class Nbt(APIView):
    def get(self, request):
        nbt = NBT()
        result = nbt.parse_rates()

        return Response(result)

