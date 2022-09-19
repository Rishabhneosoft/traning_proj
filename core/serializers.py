# # from rest_framework import serializers
# # from django.contrib.auth.models import User

# # # User Serializer
# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ('id', 'username', 'email')

# # # Register Serializer
# # class RegisterSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ('id', 'username', 'email', 'password')
# #         extra_kwargs = {'password': {'write_only': True}}

# #     def create(self, validated_data):
# #         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

# #         return user





# from rest_framework import serializers
# from core.models import User
# from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# # from core.utils import Util

# class UserRegistrationSerializer(serializers.ModelSerializer):
#   # We are writing this becoz we need confirm password field in our Registratin Request
#   password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
#   class Meta:
#     model = User
#     fields=['email', 'name', 'password', 'password2', 'tc']
#     extra_kwargs={
#       'password':{'write_only':True}
#     }

#   # Validating Password and Confirm Password while Registration
#   def validate(self, attrs):
#     password = attrs.get('password')
#     password2 = attrs.get('password2')
#     if password != password2:
#       raise serializers.ValidationError("Password and Confirm Password doesn't match")
#     return attrs

#   def create(self, validate_data):
#     return User.objects.create_user(**validate_data)