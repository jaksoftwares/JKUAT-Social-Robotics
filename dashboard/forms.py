from django import forms
from people.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'degree', 'specialty', 'bio', 'profile_picture', 'category', 'linked_in_link', 'personal_website_link']
