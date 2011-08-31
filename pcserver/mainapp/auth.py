from django.contrib.auth.backends import ModelBackend
from mainapp.models import Token
class TokenBackend(ModelBackend):
    def authenticate(self, username=None, password=None):

        try:
            token = Token.objects.get(string=password)
        except Token.DoesNotExist:
            return None
        return token.user
