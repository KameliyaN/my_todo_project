from django import forms

from profile_todo.models import Profile, Todo


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Age')
    first_name = forms.CharField(label='Fist name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    pic = forms.URLField(required=False, label='Picture', widget=forms.URLInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    passw = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = '__all__'


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Title',widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    is_done = forms.BooleanField(label='Done or not')

    class Meta:
        model = Todo
        exclude = ['user', 'prof']
        fields = ['title', 'is_done', 'description']
