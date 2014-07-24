#coding: utf-8
from __future__ import absolute_import
from rest_framework import serializers, fields

class AlgorithmsSerializer(serializers.Serializer):
    steps = serializers.CharField()
