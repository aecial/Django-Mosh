from django.forms import ModelForm
from .models import Room, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Create all fields from the form model => __all__
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('user', 'room')
        # Create all fields from the form model => __all__
        # fields = '__all__'