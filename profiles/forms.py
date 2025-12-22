# profiles/forms.py
from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'default_full_name',
            'default_email',
            'default_phone_number',
            'default_country',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy config
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Update Profile'))

        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field == 'default_country':
                self.fields[field].widget.attrs.update({
                    'aria-label': 'Country Selection',
                    'class': 'border-black rounded-0 profile-form-input'
                })
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs.update({
                    'placeholder': placeholder,
                    'class': 'border-black rounded-0 profile-form-input'
                })

            self.fields[field].label = False
