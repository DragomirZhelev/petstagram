from django import forms

from petstagram.pets.models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'pet_photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'pet_photo': forms.URLInput(attrs={'placeholder': 'Link to image'}),
        }
        labels = {
            'name' : 'Pet Name',
            'date_of_birth': 'Date of birth',
            'pet_photo': 'Link to image',
        }

class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

