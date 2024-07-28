
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import*
from .serializers import*
from rest_framework.views import APIView


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class studentapi(APIView):
  authentication_classes=[TokenAuthentication] #token authentication ya authentication
  permission_classes = [IsAuthenticated]

  def get(self,request):
     student_obj = student.objects.all()
     vic_serializer = studentserializers(student_obj, many=True)
     return Response({'status': 2000, 'message': vic_serializer.data})
  
  def post(self,request):
     
     vic_serializer = studentserializers(data=request.data)
     if vic_serializer.is_valid():
        vic_serializer.save()
        return Response({'status': 2000, 'message': vic_serializer.data})
     else:
        return Response({'status': 2000, 'errors': vic_serializer.errors})

  
  def put(self,request):
    try: 
      data=request.data
      student_obj=student.objects.get(id=request.data['id'])
      vic_serializer = studentserializers(student_obj,data=data,partial=True)
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
      student_obj=student.objects.get(id=request.data['id'])
      student_obj.delete()
      return Response({'status':'deleted'}) 
    except Exception as e:
       print(e) 
       return Response({'statuss':397,'message':'invlaid id'})




from rest_framework import viewsets
from rest_framework.decorators import action


#modelviewset ek url se sara call hoga l
class StudentViewSet(viewsets.ModelViewSet):
    
    queryset = student.objects.all()
    serializer_class = studentserializers


    @action(detail=False, methods=['post'])
    def set_section(self, request):
        
        serializer = sectionserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': serializer.data})
        else:
            return Response({'errors':serializer.errors})
        
    @action(detail=False, methods=['GET'])
    def get_section(self, request):
        obj=section.objects.all()
        serializer = sectionserializers(obj,many=True)
        return Response({"mesage":serializer.data})




    





# @api_view(['GET','POST'])

# def core(request):
#     return Response({'status':2000,
#                      'messsage':'this is vicky'})



# @api_view(['GET'])
# def vrg(request):
#     student_obj = student.objects.all()
#     vic_serializer = studentserializers(student_obj, many=True)
#     return Response({'status': 2000, 'message': vic_serializer.data})

# @api_view(['POST'])
# def vicky(request):
#     serial = studentserializers(data=request.data)
    
#     if serial.is_valid():  # Validate the serializer data
#         serial.save()  # Save the validated data to the database
#         return Response({'status': 2000, 'payload': serial.data, 'message': 'you sent'})
#     else:
#         return Response({'status': 4000, 'errors': serial.errors})


# @api_view(['POST'])
# def prince(request):
    
#     vic_serial=studentserializers(data=request.data)
  
#     if not vic_serial.is_valid():
#          return Response({'status':404,'errors':vic_serial.errors,'message':'something went wrong'})
    

#     vic_serial.save()
   
#     return Response({'status': 2000,'payload':vic_serial.data ,'message':'you sent'})


# @api_view(['PUT'])
# def update_student(request,id):

#     try:
#        student_obj=student.objects.get(id=id)
#        vic_serial=studentserializers(student_obj,data=request.data,partial=True)
  
#        if not vic_serial.is_valid():
#           return Response({'status':404,'errors':vic_serial.errors,'message':'something went wrong'})
    

#        vic_serial.save()
#        return Response({'status': 2000,'payload':vic_serial.data ,'message':'you sent'})
#     except Exception as e:

   
#         return Response({'status': 300,'error':'invlaid id','message':'you sent'})
    
# @api_view(['DELETE'])
# def delete_student(request,id):

#     try:
#        studentd=student.objects.get(id=id)
#        studentd.delete()
#        return Response({
#                           'status':340,'message':'deleted'})
       
#     except Exception as e:

   
#         return Response({'status': 300,'error':'invlaid id','message':'you sent'})





# @api_view(['GET','POST'])
# def get_book(request):
#     book_obj =Book.objects.all()
#     vic_serializer = Bookserializers(book_obj, many=True)
#     return Response({'status': 2000, 'message': vic_serializer.data})


# @api_view(['POST'])
# def get_book(request):
#     serial = bookserializers(data=request.data)
    
#     if serial.is_valid():  # Validate the serializer data
#         serial.save()  # Save the validated data to the database
#         return Response({'status': 2000, 'payload': serial.data, 'message': 'you sent'})
#     else:
#         return Response({'status': 4000, 'errors': serial.errors})



@api_view(['POST', 'GET'])
#@permission_classes([IsAuthenticated])
def postget(request): 
    
    
    if request.method == 'POST':
        serializer = todoserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 2000, 'payload': serializer.data, 'message': 'Todo created successfully'})\
            
        return Response(serializer.errors, status=400)
    
    elif request.method == 'GET':
        todo_obj = todo.objects.all()
        serializer = todoserializers(todo_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})





@api_view(['PATCH'])

def patch_todo(request):
    data=request.data
    obj=todo.objects.get(uid=data['uid'])
    serial = todoserializers(obj,data=data,partial=True)
    
    if serial.is_valid():  # Validate the serializer data
        serial.save()  # Save the validated data to the database
        return Response({'status': 2000, 'payload': serial.data, 'message': 'you sent'})
    else:
        return Response({'status': 4000, 'errors': serial.errors})

