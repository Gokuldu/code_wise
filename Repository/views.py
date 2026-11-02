from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionDb,SubmissionDb
from Repository.serializers import QuestionSerializer,SubmissionSerializer
# Create your views here.
class QuestionLIstCreateView(APIView):
    def get(self,request):
        # retrive all request from the questions model
        qs = QuestionDb.objects.all()

        serializer_instance = QuestionSerializer(qs,many=True)

        # result = list(qs)
        return Response(data=serializer_instance.data)
        
    def post(self,request):
        
       from_data = request.data

       serializer_instance = QuestionSerializer(data=from_data)

       if serializer_instance.is_valid():

            orginal_data = serializer_instance.validated_data
        
            QuestionDb.objects.create(**orginal_data)
            return Response(data=serializer_instance.data)
       else:
            return Response(data=serializer_instance.errors)
  
class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):  #(parameter) pk=primary key

        qs = QuestionDb.objects.get(id=pk)

        serializer_instance = QuestionSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def put(self,request,pk):

        from_data = request.data
        serializer_instance = QuestionSerializer(data=from_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            QuestionDb.objects.filter(id=pk).update(**actual_data)

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):

        QuestionDb.objects.filter(id=pk).delete()

        return Response(
            {"message":"question deleted successfully....!"}
        )

class SubmissionLIstCreateView(APIView):

    def get(self, request):
        qs = SubmissionDb.objects.all()
        serializer_instance = SubmissionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        serializer_instance = SubmissionSerializer(data=request.data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            SubmissionDb.objects.create(**actual_data)

            return Response(
                data=serializer_instance.data,
                status=201
            )

        return Response(
            data=serializer_instance.errors,
            status=400
        )
# class SubmissionLIstCreateView(APIView):
#     def get(self,request):
#         qs = SubmissionDb.objects.all()
#         serializer_instance = SubmissionSerializer(qs,many=True)
#         return Response(data=serializer_instance.data)

   
# def post(self, request):
#     from_data = request.data

#     serializer_instance = SubmissionSerializer(data=from_data)

#     if serializer_instance.is_valid():
#         actual_data = serializer_instance.validated_data

#         SubmissionDb.objects.create(**actual_data)

#         return Response(data=serializer_instance.data, status=201)

#     return Response(data=serializer_instance.errors, status=400)



class SubmissionRetrieveUpdateView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(SubmissionDb,id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)



class EvaluateSubmissionView(APIView):

    def put(sefl,request,pk):

        from_data = request.data

        SubmissionDb.objects.filter(id=pk).update(**from_data)

        return Response(data={
            "message": "updated"
        })