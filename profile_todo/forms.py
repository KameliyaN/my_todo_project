from django import forms
from django.core.exceptions import ValidationError
from profile_todo.models import Profile, Todo
from django.core.validators import MinValueValidator, URLValidator, EmailValidator, RegexValidator, MinLengthValidator


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=False, validators=[MinValueValidator(1), ],
                             widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Age',
                             )
    first_name = forms.CharField(label='Fist name',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pic = forms.URLField(required=False, label='Picture', widget=forms.URLInput(attrs={'class': 'form-control'}),
                         validators=[URLValidator()])
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}), )
    passw = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                            validators=[RegexValidator(r'[a-zA-Z\d]'), MinLengthValidator(6)])

    class Meta:
        model = Profile
        fields = '__all__'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        comr_name = [x for x in first_name if x.isalpha()]
        if len(first_name) > len(comr_name):
            raise ValidationError('First name must include only letters')
        if not first_name[0].isupper():
            raise ValidationError('First letter must be uppercase letter')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        comr_name = [x for x in last_name if x.isalpha()]
        if len(last_name) > len(comr_name):
            raise ValidationError('First name must include only latin letters')
        if not last_name[0].isupper():
            raise ValidationError('First letter must be uppercase letter')
        return last_name


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    is_done = forms.BooleanField(label='Done or not')

    class Meta:
        model = Todo
        exclude = ['user', 'prof']
        fields = ['title', 'is_done', 'description']

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title[0].isupper():
            raise ValidationError('Title must starts with uppercase letter')
        letters_title = [x for x in title if x.isalpha()]
        if len(title) > len(letters_title):
            raise ValidationError('Title must contain only letters')
        return title
