from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from .models import List
from tastypie.serializers import Serializer


class ListResource(ModelResource):
    class Meta:
        queryset = List.objects.all()
        resource_name = 'list'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

        serializer = Serializer()
