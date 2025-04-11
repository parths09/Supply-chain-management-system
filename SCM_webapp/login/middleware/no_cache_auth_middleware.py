from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class NoCacheAndAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        protected_paths = ['/customer/', '/manager/', '/supplier/']
        for path in protected_paths:
            if request.path.startswith(path) and not request.user.is_authenticated:
                return redirect('/')

    def process_response(self, request, response):
        # Force no browser cache
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
