from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from repository import models
from api.utils.response import BaseResponse


from api.serializers.network import NetworkSerializer
from api.utils.serialization_general import SerializedData
from api.utils.auth import Authentication
import json


class NetworkView(ViewSetMixin, APIView):
    def get_msg(self, request,pk, *args, **kwargs):
        """
        主机详情
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        queryset = models.Network.objects.filter(host_id=pk)
        # print(queryset.values())
        serializer_class = NetworkSerializer
        data = SerializedData(request, queryset, serializer_class).get_data()
        # print(data)
        return HttpResponse(json.dumps(data))
        # return Response(data)