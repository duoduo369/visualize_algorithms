from __future__ import absolute_import
from rest_framework.views import APIView
from random import shuffle
from algorithms.api import run
from api.serializers import AlgorithmsSerializer
from rest_framework import status
from rest_framework.response import Response
from importlib import import_module
from django.http import Http404
from api.models import AlgoResult

class SingleArrayInPlaceAlgorithmView(APIView):

    def get(self, request, algorithm_name):
        seq = request.GET.get('seq', None)
        kwargs = {'seq': seq} if seq else {}
        result = AlgoResult(steps=list(run(algorithm_name, **kwargs)))
        seri = AlgorithmsSerializer(result)
        return Response(seri.data)
