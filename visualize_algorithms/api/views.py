from __future__ import absolute_import
from rest_framework.views import APIView
from random import shuffle
from api.conf import ALGORITHM_MAPPER
from api.serializers import AlgorithmsSerializer
from rest_framework import status
from rest_framework.response import Response
from importlib import import_module
from django.http import Http404
from api.models import AlgoResult

SEQ = range(100)
shuffle(SEQ)

class SingleArrayInPlaceAlgorithmView(APIView):

    def get(self, request, algorithm_name):
        try:
            mapper = ALGORITHM_MAPPER[algorithm_name]
            module = import_module(mapper['module'])
            method = getattr(module, mapper['method'])
        except KeyError:
            raise Http404
        seq = request.GET.get('seq', SEQ)
        result = AlgoResult(steps=list(method(seq)))
        seri = AlgorithmsSerializer(result)
        return Response(seri.data)
