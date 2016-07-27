from django.conf import settings
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    def get(self, request: Request) -> Response:
        return Response(status=status.HTTP_200_OK, data={
            'message': settings.HELLO_WORLD_TEXT
        })