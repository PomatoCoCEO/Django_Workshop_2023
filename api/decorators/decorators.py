import functools
from django.http import JsonResponse, HttpRequest

# create a decorator to verify the methos

def method(*methods):
    @functools.wraps(methods)
    def decorator(func):
        def wrapper(request:HttpRequest, *args, **kwargs):
            if request.method not in methods:
                return JsonResponse({'message': 'Method not allowed'}, status=405)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator