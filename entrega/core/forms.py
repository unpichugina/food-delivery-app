from django import forms
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'address')

    def clean_phone(self):
        if not self.cleaned_data['phone'].isdigit():
            raise forms.ValidationError('Phone format is wrong.')
        return self.cleaned_data['phone']

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match')
        return password_confirm

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

