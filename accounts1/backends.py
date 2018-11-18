from django.contrib.auth.models import User


class EmailAuth:
    """Authenticate a user by an exact match on the email and password."""
    
    def authenticate(self, username=None, password=None):
        """
        Get instance of `User` based on the email and verify the 
        password.
        """
            
        try:
            user = User.objects.get(email=username)
            # We are using username because that is the name of the element in the form.
            
            if user.check_password(password):
                return user
            return None
        
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """Used by Django authentication system to retrieve a user instance."""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
            
    