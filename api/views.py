from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import os

class SomeAPI(APIView):
    def get(self, request, *args, **kwargs):
        context = []
        for root, folder, files in os.walk("./jobtest"):  
            for filename in files:
                dict = {"name": filename,
                        "type":"file",
                        "time":os.path.getctime(root)
                        }
                context.append(dict)
            for folders in folder:
                dict = {"name": folders,
                        "type":"folder",
                        "time":os.path.getctime(root)
                        }
                context.append(dict)
        return Response({'data':context})