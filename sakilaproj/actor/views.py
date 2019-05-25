from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from .models import Actor
from rest_framework import generics, status
from .serializer import ActorSerializer
from .decorators import validate_request_data


class ActorList(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ListCreateSongsView(generics.CreateAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_actor = Actor.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            last_update=request.data["last_update"]
        )
        return Response(
            data={"message": "Actor created successfully.",
                  "success": "True", "data":
                      ActorSerializer(a_actor).data},
            status=status.HTTP_201_CREATED
        )
