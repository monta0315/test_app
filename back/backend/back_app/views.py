from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def res_luck(request):
  num = 0
  if num == 0:
    return Response("Luckey", status=status.HTTP_201_CREATED)
  elif num == 1:
    return Response("Super Lucky", status=status.HTTP_201_CREATED)
  else:
    return Response("Bad", status=status.HTTP_201_CREATED)
