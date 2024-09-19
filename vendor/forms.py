from django import forms
from .models import Vendor
from accounts.validators import allow_only_images_validator
class VerdorForm(forms.ModelForm):
    vendor_license = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn-btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model = Vendor
        fields = ['verdor_name','vendor_license']