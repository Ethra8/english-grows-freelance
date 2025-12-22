
from django import forms
from .widgets import CustomClearableFileInput
from .models import IndivService, IndividualType


class IndivServiceForm(forms.ModelForm):

    class Meta:
        model = IndivService
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = IndividualType.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in types]

        self.fields['name'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
