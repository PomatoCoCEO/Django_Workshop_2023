from django.http import HttpRequest, JsonResponse
import json
from ..models import User
import bcrypt
from ..decorators.decorators import method

@method('POST')
def register_user(request :HttpRequest):
    body = json.loads(request.body)
    print(body)
    username = body['username']
    password = body['password']


    # check if the username already exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({'message': 'Username already exists'}, status=400)

    # create user in database
    user = User(username=username, password=password)
    user.save()

    # return a 201 response
    return JsonResponse({'message': 'User created'}, status=201)



def login_user(request :HttpRequest):
    pass