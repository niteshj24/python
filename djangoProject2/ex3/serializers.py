from rest_framework import serializers
from ex3.models import routerapi

class RouterSrtislizer(serializers.ModelSerializer):
    sapid = serializers.CharField(required=False)
    hostname = serializers.CharField(required=False)
    macip = serializers.CharField(required=False)
    loopback = serializers.CharField(required=False)

    class Meta:
        model = routerapi
        fields = '__all__'
