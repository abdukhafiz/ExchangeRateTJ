from datetime import datetime

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from parsers.api.alif import Alif as AlifBank
from parsers.xml.nbt import Nbt as NBT
from parsers.web_scrap.eskhata import Eskhata as ESKHATA
from parsers.web_scrap.spitamen import Spitamen as SPITAMEN
from parsers.api.amonat import Amonat as AMONAT
from parsers.api.arvand import Arvand as ARVAND
from parsers.web_scrap.imon import Imon as IMON
from parsers.web_scrap.humo import Humo as HUMO


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


class Amonat(APIView):
    def get(self, request):
        amonat = AMONAT()
        result = amonat.parse_rates()

        return Response(result)


class Arvand(APIView):
    def get(self, request):
        arvand = ARVAND()
        result = arvand.parse_rates()

        return Response(result)


class Imon(APIView):
    def get(self, request):
        imon = IMON()
        result = imon.parse_rates()

        return Response(result)


class Humo(APIView):
    def get(self, request):
        humo = HUMO()
        result = humo.parse_rates()

        return Response(result)
