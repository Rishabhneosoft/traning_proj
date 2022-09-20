from rest_framework import serializers
from core.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    mobile_number= serializers.CharField(style={'input_type': 'phonenumber'},write_only=True)

    class Meta:
        model = User
        fields = ['email','username','mobile_number','password','password2']
        extra_kwargs = {
            'password': {'write_only':True},
            'mobile_number': {'write_only':True},
        }

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            mobile_number = self.validated_data['mobile_number'],

        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':Password})
        account.set_password(password)
        account.save()
        return account 


from django.contrib.auth import authenticate

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        # phone = attrs.get('phone_number')
        # if User.objects.filter(mobile_number=phone):
        #     raise serializers.ValidationError(
        #         'The phone number is already registered.')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
# def validate(self, attrs):
#         phone = attrs.get('phone_number')
#         if User.objects.filter(phone_number=phone):
#             raise serializers.ValidationError(
#                 'The phone number is already registered.')
#         return attrs   