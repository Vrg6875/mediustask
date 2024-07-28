from rest_framework import serializers
from .models import*




class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        #exclude=['id']
        #fields=['name']

class sectionserializers(serializers.ModelSerializer):
   
    class Meta:
        model = section
        fields = '__all__'    
        #exclude=['uid','created_at']
       

    # def validate(self,data):
    #    if data['age']<18: 
    #     raise serializers.ValidationError({'error':'age can not be less than 18'})   
    
    #    if data['name']:
    #       for n in data['name']:
    #          if n.isdigit():
    #             raise serializers.ValidationError({'error':'name can not be number'})

class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Bookserializers(serializers.ModelSerializer):
    category=Categoryserializers()
    class Meta:
        model = Book
        fields = '__all__'       


from core.models import todo

class todoserializers(serializers.ModelSerializer):
   
    class Meta:
        model = todo
        fields = '__all__'    
        #exclude=['uid','created_at']

    def validate(self, data):
        title = data.get('todo_title', None)
        if title and len(title) < 3:
            raise serializers.ValidationError('todo title must be more than 3 characters')   
        return data
    
class companyserializers(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'    