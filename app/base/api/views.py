from datetime import datetime

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from parsers.api.alif import Alif as AlifBank
from parsers.xml.nbt import Nbt as NBT
from parsers.web_scrap.eskhata import Eskhata as ESKHATA
from parsers.web_scrap.spitamen import Spitamen as SPITAMEN


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


class Eskhata(APIView):
    def get(self, request):
        eskhata = ESKHATA()
        result = eskhata.parse_rates()

        return Response(result)


class Spitamen(APIView):
    def get(self, request):
        spitamen = SPITAMEN()
        result = spitamen.parse_rates()

        return Response(result)
