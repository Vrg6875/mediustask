from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])

def home(request):
    if request.method=='GET':
        return Response({
            'status':200,
            'method called':'get'
        })
    elif request.method=='POST':
        return Response({
            'status':300,
            'method called':'POST'
        })

