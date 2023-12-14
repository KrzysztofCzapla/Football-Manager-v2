from rest_framework import serializers
from apps.common.models import Country

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name')
