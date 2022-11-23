from .models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, DateInput, Select,ChoiceField
class UserForm(ModelForm):
   class Meta: 
      model = User
      fields = '__all__'
      position = ChoiceField(required=True)
      widgets = {
            'userName' : TextInput(attrs={
            'class' : 'register_input',
            'placeholder':'성함을 입력해주세요.'
         }),
            'birthday' : DateInput(attrs={
            'placeholder':'생년월일을 입력해주세요.', 
            'class': 'register_input',
            'type': 'date'   
         }),
            'nickname' : TextInput(attrs={
            'class' : 'register_input',
            'placeholder':'별명을 입력해주세요.'
         }),
            'password' : PasswordInput(attrs={
            'class' : 'register_input',
            'placeholder':'비밀번호를 입력해주세요.'
         }),
            'emailAddress' : TextInput(attrs={
            'class' : 'register_input',
            'placeholder':'이메일을 입력해주세요.'
         }),
            'userGender' : Select(attrs = {
               'class':'register_input',
               'placeholder':'성별을 입력해주세요.'
            })
      }
      required = {
         'userGender' : True
      }
      labels = {
         'nickname':'',
         'password':'',
         'userName':'',
         'emailAddress':'',
         'birthday' : '',
         'userGender' : ''
      }