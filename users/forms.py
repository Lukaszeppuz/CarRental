from . import models
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = models.Customer
        # exclude = ['id']
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'birth_date', 'identity_document_type', 'identity_document_no']
        # fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']