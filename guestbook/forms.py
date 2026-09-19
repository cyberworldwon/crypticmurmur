from django import forms

MAX_IMAGE_SIZE = 5 * 1024 * 1024

ALLOWED_IMAGE_TYPES = {
    'image/jpeg',
    'image/png',
    'image/gif',
}

class EntryForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='Your name',
        required=False
    )

    message = forms.CharField(
        max_length=300,
        label='Message',
        widget=forms.Textarea,
        required=False
    )

    image = forms.ImageField(
        required=False,
        label='Image'
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if not image:
            return image

        if image.size > MAX_IMAGE_SIZE:
            raise forms.ValidationError(
                'Image must be smaller than 5 MB.'
            )

        if image.content_type not in ALLOWED_IMAGE_TYPES:
            raise forms.ValidationError(
                'Only JPEG, PNG and GIF images are allowed.'
            )

        return image