#rest-framework imports
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import Serializer
#end rest framework imports

from .serializers import ObservationSerializer
from .predict import loanpredictfunc

@api_view['POST']
def predict_view(request):
    serializer = Serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        response = loanpredictfunc(serializer)
        Response(response, status=HTTP_200_OK)