from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import*
from .serializers import*

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

 
 
@api_view(['GET'])
def ipl_get(request):
    ipl_obj = ipl.objects.all()
    serializer = iplserializers(ipl_obj, many=True)
    return Response({'status': 2000, 'message': serializer.data})


@api_view(['POST'])
def ipl_post(request):
   data=request.data
   vic_serializer=iplserializers(data=request.data)
   if vic_serializer.is_valid():
       vic_serializer.save()
       return Response({'data':vic_serializer.data})
   else:
       return Response({'error':vic_serializer.errors})
   


@api_view(['PATCH'])
def ipl_patch(request,id):
   
#    ipl_obj=ipl.objects.get(id=id)
#    vic_serializer=iplserializers(ipl_obj,data=request.data,partial=True)
#    if vic_serializer.is_valid():
#        vic_serializer.save()
#        return Response({'data':vic_serializer.data})
#    else:
#        return Response({'error':vic_serializer.errors})
 

    try:
       student_obj=ipl.objects.get(id=id)
       vic_serial=iplserializers(student_obj,data=request.data,partial=True)
  
       if not vic_serial.is_valid():
          return Response({'status':404,'errors':vic_serial.errors,'message':'something went wrong'})
    

       vic_serial.save()
       return Response({'status': 2000,'payload':vic_serial.data ,'message':'you sent'})
    except Exception as e:

   
        return Response({'status': 300,'error':'invlaid id','message':'you sent'})
    
@api_view(['DELETE'])
def ipl_delete(request,id):

    try:
       studentd=ipl.objects.get(id=id)
       studentd.delete()
       return Response({
                          'status':340,'message':'deleted'})
       
    except Exception as e:

   
        return Response({'status': 300,'error':'invlaid id','message':'you sent'})


from rest_framework import viewsets
from rest_framework.decorators import action
class iplViewSet(viewsets.ModelViewSet):
    
    queryset = ipl.objects.all()
    serializer_class = iplserializers
    @action(detail=False, methods=['post'])
    def set_color(self, request):
        
        serializer = iplcolorserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': serializer.data})
        else:
            return Response({'errors':serializer.errors})
        




from rest_framework.views import APIView
 
class iplapi(APIView):
  #authentication_classes=[TokenAuthentication] #token authentication ya authentication
  #permission_classes = [IsAuthenticated]

  def get(self,request):
     student_obj = ipl.objects.all()
     vic_serializer = iplserializers(student_obj, many=True)
     return Response({'status': 2000, 'message': vic_serializer.data})
  
  def post(self,request):
     
     vic_serializer = iplserializers(data=request.data)
     if vic_serializer.is_valid():
        vic_serializer.save()
        return Response({'status': 2000, 'message': vic_serializer.data})
     else:
        return Response({'status': 2000, 'errors': vic_serializer.errors})

  
  def put(self,request):
    try: 
      data=request.data
      student_obj=ipl.objects.get(id=request.data['id'])# here also use id=request.data.get('id)
      vic_serializer = iplserializers(student_obj,data=data,partial=True)
      if vic_serializer.is_valid():
        vic_serializer.save()
        return Response({'status': 2000, 'message': vic_serializer.data})
      else:
        return Response({'status': 2000, 'errors': vic_serializer.errors}) 
    except Exception as e:
       print(e) 
       return Response({'statuss':397,'message':'invlaid id'})




  def delete(self,request):
    try: 
      student_obj=ipl.objects.get(id=request.data['id'])
      student_obj.delete()
      return Response({'status':'deleted'}) 
    except Exception as e:
       print(e) 
       return Response({'statuss':397,'message':'invlaid id'})

       
        
