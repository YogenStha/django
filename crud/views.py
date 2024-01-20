from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer,TeacherSerializer
from .models import Student,Teacher

# Create your views here
# def postStudent(request):
#     data = request.data
#     return Response(data)
@api_view(['POST'])
def postStudent(request):
    try:
        request_data = request.data
        print(request_data)
        serializer = StudentSerializer(data=request_data,many= False)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({'message':"student added successfully"})
    except Exception as e:
        return Response(e)

@api_view(['POST'])
def postTeacher(request):
    try:
        request_data = request.data
        print(request_data)
        serializer = TeacherSerializer(data=request_data,many= False)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({'message':'teacher added successfully'})
    except Exception as e:
        return Response(e)

@api_view(['GET'])
def getStudent(request):
    try:
        students = Student.objects.all()
        serializer_data = StudentSerializer(students, many=True)
        return Response(serializer_data.data)
    except Exception as e :
        return Response(str(e))

@api_view(['GET'])
def getTeacher(request):
    try:
        teacher = Teacher.objects.all()
        serializer_data = TeacherSerializer(teacher, many=True)
        return Response(serializer_data.data)
    except Exception as e :
        return Response(str(e))

@api_view(['POST'])
def editStudentData(request,id):
    student = Student.objects.get(id=id)
    serializer_data = StudentSerializer(student, data=request.data,many = False,partial =True)
    if serializer_data.is_valid(raise_exception=True):
        serializer_data.save()
    return Response({"message":'student Data has been updated'})

@api_view(['GET'])
def editStudentData(request,id):
    student = Student.objects.get(id=id)
    serialized_data = StudentSerializer(student,many =False)
    return Response(serialized_data.data)

@api_view(['POST'])
def editTeacherData(request,id):
    teacher = Teacher.objects.get(id=id)
    serializer_data = TeacherSerializer(teacher, data=request.data,many = False,partial =True)
    if serializer_data.is_valid(raise_exception=True):
        serializer_data.save()
    return Response({"message":'Teacher Data has been updated'})

# @api_view(['POST'])
# def updateStudentData(request,id):
#     try:
#         student =Student.objects.get(id=id)
#         serializer_data = StudentSerializer(student,many = False,data=True)
#         if serializer_data.is_valid(raise_exception=True):
#             serializer_data.save()
#             return Response({"message":'data updated successfully',"data": serializer_data.data})
#     except Exception as e:
#         return Response({"err":e})
@api_view(['GET'])
def deleteStudentData(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message":'this item is deleted std'})

@api_view(['GET'])
def deleteTeacherData(request,id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return Response({"message":'this item is deleted teacher'})