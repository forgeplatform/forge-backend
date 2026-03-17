# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

from forge.api.generics import RetrieveAPIView, SimpleListAPIView
from forge.api import serializers
from forge.main import models


class ActivityStreamList(SimpleListAPIView):
    model = models.ActivityStream
    serializer_class = serializers.ActivityStreamSerializer
    search_fields = ('changes',)


class ActivityStreamDetail(RetrieveAPIView):
    model = models.ActivityStream
    serializer_class = serializers.ActivityStreamSerializer
