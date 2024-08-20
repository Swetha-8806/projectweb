from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class betacls(APIView):
    def post(self):
        value = request.data.get('value')


        
        return Response("Hey Buddy")
