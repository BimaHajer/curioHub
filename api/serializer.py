from rest_framework import serializers
from userManagement.models import UserApp
class UserAPPSerializer (serializers.ModelSerializers):
    class Meta:
      model=UserApp
      fields = ["__all__"]
