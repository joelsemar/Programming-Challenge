from django.contrib.auth import login, authenticate, logout
import logging
from random import randint
from django.http import HttpResponse
import time
import datetime
logger = logging.getLogger('webservice')
logger.debug
class PCMiddleware(object):
    def process_request(self, request):
        key = request.GET.get('key')
        user = authenticate(password=key)
        if user is not None:
            logger.debug("%s -- %s requested: %s" % (datetime.datetime.utcnow(), user.username, request.path+'?'+request.META['QUERY_STRING']))
            login(request, user)
            roll = randint(1,10)
            if roll == 3:
                return HttpResponse("Internal Server Error", status=500)
            if roll == 4:
                time.sleep(400)
        return None

    def process_response(self, request, response):
        if not request.user.is_superuser:
            logout(request)
            return response
