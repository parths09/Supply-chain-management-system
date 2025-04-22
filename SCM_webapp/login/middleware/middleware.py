from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User

# class NoCacheAndAuthMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         protected_paths = ['/customer/', '/manager/', '/supplier/',]
#         for path in protected_paths:
#             if request.path.startswith(path) and not request.user.is_authenticated:
#                 return redirect('/')

#     def process_response(self, request, response):
#         # Force no browser cache
#         response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
#         response['Pragma'] = 'no-cache'
#         response['Expires'] = '0'
#         return response

# middleware.py

class MultiRoleSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Always allow access to simulation without role checks
        if request.path.startswith('/simulation/'):
            return None
        
        # Skip for login and register pages
        if request.path in ['/', '/register/', '/login/']:
            return None
            
        # Check if a role is specified in the URL
        role = request.GET.get('as_role', None)
        
        # If no role specified but path starts with a role directory, extract the role
        if not role:
            role_paths = ['customer', 'supplier', 'manager',]
            for path in role_paths:
                if request.path.startswith(f'/{path}/'):
                    role = path
                    break
        
        # If we have a role and role sessions exist
        if role and 'role_sessions' in request.session:
            # Check if user has authenticated for this role
            if role in request.session['role_sessions']:
                user_id = request.session['role_sessions'][role]
                try:
                    # Set the user to the role-specific user
                    request.session_role = role
                    request.original_user = request.user
                    request.user = User.objects.get(id=user_id)
                except User.DoesNotExist:
                    # If user no longer exists, remove from role sessions
                    del request.session['role_sessions'][role]
                    request.session.modified = True
                    
                    # Redirect to login if path requires authentication
                    protected_paths = ['/customer/', '/manager/', '/supplier/',]
                    if any(request.path.startswith(path) for path in protected_paths):
                        return redirect(f'/login/?next={request.path}&as_role={role}')
            else:
                # If not authenticated for this role, redirect to role-specific login
                protected_paths = ['/customer/', '/manager/', '/supplier/', ]
                if any(request.path.startswith(path) for path in protected_paths):
                    return redirect(f'/login/?next={request.path}&as_role={role}')
        
        return None

    def process_response(self, request, response):
        # No cache for all responses to avoid session conflicts
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    
class SimulationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Only process simulation requests
        if not request.path.startswith('/simulation/'):
            return None
            
        # No role needed for simulation
        # You could use a simulation-specific session if needed
        if 'simulation_session' not in request.session:
            request.session['simulation_session'] = {}
            
        return None