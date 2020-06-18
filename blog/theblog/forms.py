from django import forms
from .models import Post, Category

#choices = [(), (), ()]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'This is a name of blog' }),
            'author': forms.TextInput(attrs={ 'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden' }),
            'category': forms.Select(choices=choice_list, attrs={ 'class':'form-control'}),
            'body': forms.Textarea(attrs={ 'class':'form-control', 'placeholder':'This is a content od Post' }),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title', 'category','body')
        widgets = {
            'title': forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'This is a name of blog' }),
            'category': forms.Select(choices=choice_list, attrs={ 'class':'form-control'}),
            'body': forms.Textarea(attrs={ 'class':'form-control', 'placeholder':'This is a content od Post' }),
        }