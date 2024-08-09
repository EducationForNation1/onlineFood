from django import forms
from .models import Vendor
class VerdorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['verdor_name','vendor_license']