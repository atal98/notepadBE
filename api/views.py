from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import NoteSerializer
from .models import Note
from rest_framework import status

class Routes(APIView):
    def get(self, request):
        response = [
            {
                'Endpoint': '/notes/',
                'method': 'GET',
                'body': None,
                'description': 'Returns an array of notes'
            },
            {
                'Endpoint': '/notes/id',
                'method': 'GET',
                'body': None,
                'description': 'Returns a single note object'
            },
            {
                'Endpoint': '/notes/create/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Creates new note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/update/',
                'method': 'PUT',
                'body': {'body': ""},
                'description': 'Creates an existing note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/delete/',
                'method': 'DELETE',
                'body': None,
                'description': 'Deletes and exiting note'
            }
        ]
        
        return Response(response)


class NotesAPI(APIView):
    
    def get(self,request):
        note_qs = Note.objects.all().order_by('-updated')

        serializer = NoteSerializer(note_qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        note_qs = Note.objects.create(body = data['body'])
        serializer = NoteSerializer(note_qs, many=False)
        return Response(serializer.data)
    
class NoteAPI(APIView):
    
    def get(self,request,pk):
        note_qs = Note.objects.get(id=pk)
        serializer = NoteSerializer(note_qs, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk):
        note_qs = Note.objects.get(id=pk)
        serializer = NoteSerializer(note_qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        note_qs = Note.objects.get(id=pk)
        note_qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
