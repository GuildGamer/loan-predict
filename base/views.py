#rest-framework imports
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.serializers import Serializer
#end rest framework imports

from .serializers import ObservationSerializer
from .predict import loanpredictfunc
from .create_model import create
import os.path

@api_view(['POST'])
def predict_view(request):
    serializer = ObservationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        if os.path.isfile('Pickle_RL_Model.pkl') == False:
            create()
        response = loanpredictfunc(serializer.validated_data)
        stat=status.HTTP_200_OK
        serializer.save()
    except ValidationError as e:
        response = e 
        stat=status.HTTP_400_BAD_REQUEST
    return Response(response, stat)