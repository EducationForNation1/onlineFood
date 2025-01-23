from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    print(ext)  # For debugging purposes
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if ext.lower() not in valid_extensions:  # Use `not in` to check against the list
        raise ValidationError('Unsupported file extension. Allowed extensions are: ' + ', '.join(valid_extensions))
