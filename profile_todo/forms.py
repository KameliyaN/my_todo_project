from django import forms

from profile_todo.models import Profile, Todo


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=False, help_text='Enter your age', widget=forms.NumberInput(), label='Age')
    first_name = forms.CharField(help_text='Enter your first name', label='Fist name')
    last_name = forms.CharField(help_text='Enter your last name', label='Last name')
    picture = forms.URLField(required=False,help_text='Enter your picture here', label='Picture', widget=forms.URLInput())
    email = forms.EmailField(help_text='Enter your email here', label='Email', widget=forms.EmailInput())
    password = forms.CharField(help_text='Enter your password here', label='Password', widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = '__all__'


class TodoForm(forms.ModelForm):
    title = forms.CharField(help_text='Todo title', label='Title')
    description = forms.CharField(label='Description', widget=forms.Textarea())
    is_done = forms.BooleanField(label='Done or not', widget=forms.CheckboxInput())

    class Meta:
        model = Todo
        exclude = ['user', 'prof']
        fields = ['title', ' description', 'is_done']
