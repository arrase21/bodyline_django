from rest_framework.viewsets import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request):
        return Response({"message": "hello world"})
