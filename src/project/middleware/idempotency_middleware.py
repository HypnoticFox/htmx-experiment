from django.conf import settings
from django.core.cache import caches
from django.http import HttpResponseBadRequest

def generate_request_hash(request):
    session_id = str(request.session.session_key)
    url_path = str(request.get_full_path())
    body_length = str(request.META["CONTENT_LENGTH"])
    
    request_hash = hash(str(len(session_id)) + session_id + str(len(url_path)) + url_path + str(len(body_length)) + body_length)
    
    print(session_id)
    print(url_path)
    print(body_length)
    
    return request_hash
    

class IdempotencyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        if request.method != "GET":
            request_hash = generate_request_hash(request)
            print(f"Request hash: '{request_hash}'")
            
            cache = caches["default"]
            
            success = cache.add(request_hash, None, settings.CACHE_IDEMPOTENCY_TIMEOUT)
            
            if not success:
                print("Idempotency key already exists in cache.")
                return HttpResponseBadRequest("Idempotency key already exists in cache.")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        
        return response