from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Import AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        }
        
        
        
        
# Search Form
class SearchForm(forms.Form):
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Enter city'})
    )
    min_price = forms.DecimalField(
        label='Min Price',
        widget=forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Min price'})
    )
    max_price = forms.DecimalField(
        label='Max Price',
        widget=forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': 'Max price'})
    )
    star_rating = forms.IntegerField(
        label='Star Rating',
        widget=forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'placeholder': '1 to 5'})
    )
