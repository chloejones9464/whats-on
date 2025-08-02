from allauth.account.forms import SignupForm
from django import forms
from accounts.models import Profile


class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ("public", "Public"),
        ("bar", "Bar Owner"),
    ]

    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        label="Who are you signing up as?",
    )

    def save(self, request):
        user = super().save(request)

        profile, created = Profile.objects.get_or_create(user=user)
        profile.user_type = self.cleaned_data["user_type"]
        profile.save()

        return user
