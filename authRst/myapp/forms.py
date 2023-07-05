from django import forms
from .models import MyUser


class MyUserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self,*args,**keyargs ):
            super(MyUserForm,self).__init__(*args,**keyargs)
            self.fields['name'].widget = forms.TextInput()
            self.fields['email'].widget = forms.EmailInput()
            self.fields['password'].widget = forms.PasswordInput()
          
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'password']
        

    