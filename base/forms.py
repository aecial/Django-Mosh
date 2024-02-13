from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Create all fields from the form model => __all__
        fields = '__all__'