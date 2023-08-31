from django.http import HttpResponse
from rest_framework.views import APIView


class Test(APIView):
    """
    Test View
    """

    def get(self, request):
        return HttpResponse('Hello test')
