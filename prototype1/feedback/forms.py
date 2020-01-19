from django import forms
from feedback.models import Post

class ScoreForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your score on scale of 1 to 10..'}))

	class Meta:
		model = Post	
		fields= ['post']