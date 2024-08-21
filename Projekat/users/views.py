from rest_framework.views import APIView
from users.service import UserService
from django.http import HttpResponse
import json
from django.core import serializers

"""
Ovde se nalazi logika za get post put i delete indexne stranice.
Na ovaj nacin cemo uraditi kompletnu aplikaciju. Dodavacemo novu
klasu ukoliko nam je potrebno nesto specificno
"""
class Index(APIView):
    def __init__(self):
        self.res = UserService()
    
    def get(self, _):
        test = self.res.getUser()

        data = serializers.serialize('json', test)
        print(data)
        return createResponse(data, 200)
    
def createResponse(responseObject, status):
    response = HttpResponse(json.dumps(
        responseObject), content_type="application/json", status=status)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response