from django import forms
from onetimesecret.models import Secret


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SecretForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Secret
        fields = ('text', 'days',)
