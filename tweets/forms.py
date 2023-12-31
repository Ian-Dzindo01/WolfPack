from django import forms
from .models import Tweet

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

MAX_POST_LENGTH = 300           # max length a post can be 

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']               # will add image here

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_POST_LENGTH:               # if post too long throw error
            raise forms.ValidationError("Post too long. Please try writing a shorter post.")
        return content

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")        # password confirm

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)        # super used to give access to methods of parent class
		user.email = self.cleaned_data['email']                   # remove extra spaces and such
		if commit:                                      # commit after cleaning
			user.save()
		return user