from django import forms
from django.contrib.auth.models import User

class SuperUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user
