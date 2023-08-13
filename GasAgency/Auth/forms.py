from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer, CustomerRepresentative


class CustomerForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('address',)


class CustomerRepresentativeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomerRepresentative
        fields = UserCreationForm.Meta.fields


class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = Customer
        

class CustomerRepresentativeLoginForm(AuthenticationForm):
    class Meta:
        model = CustomerRepresentative

