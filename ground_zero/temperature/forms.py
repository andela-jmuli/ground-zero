from django.forms import ModelForm, Textarea
from models import Temperature


class TemperatureForm(ModelForm):
    """ Form for temperature input """
    class Meta:
        model = Temperature
        fields = ['temp_value']
