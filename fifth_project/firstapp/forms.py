from django import forms
from django.core import validators


class Contact_Form(forms.Form):
    name = forms.CharField(initial="hellow",help_text="enter your name",required=False,widget=forms.Textarea(attrs={'id':'usernamid','class':'usernameclass1 usernameclass2 ','placeholder':"enter yourname",'cols':1,'rows':1}))
    email = forms.EmailField()
    age = forms.IntegerField()
    weight=forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appoiment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    ipa = forms.GenericIPAddressField()
    CHOICE = (('s','burger'),('l','senwdice'),('xt','pizza'),('xxt','big pizza'))
    choicefield = forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    CHOICE = (('s','burger'),('l','senwdice'),('xt','pizza'),('xxt','big pizza'))
    multiplechoicefield = forms.MultipleChoiceField(choices=CHOICE,widget=forms.CheckboxSelectMultiple)
    # file = forms.FileField()
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)

  
#     def clean(self):
#         cleaned_data = super().clean()
#         print(cleaned_data)
#         name = self.cleaned_data['name']
#         email = self.cleaned_data['email']
#         if len(name) < 6 :
#             raise forms.ValidationError("enter your name must be 6 or gather than")

#         if '.com' not in email:
#             raise forms.ValidationError("email must be include '.com'")
        
       
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,"inter your name most 10 characthers"),validators.MinLengthValidator(5,'enter your name must be 5 characthers')])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="enter valid email address")])
    age = forms.IntegerField(widget=forms.NumberInput,validators=[validators.MinValueValidator(18,message="enter value must be equal or gather than 18"),validators.MaxValueValidator(100,message="enter value must be less than or equal 100")])
    blance = forms.DecimalField(validators=[validators.DecimalValidator(5,2)])
    file = forms.FileField(validators=[validators.FileExtensionValidator(['png','jpeg','zip'],message="this fild only store the file extenstion 'png','jpen,,")])



class PasswardMatchProject(forms.Form):
     name = forms.CharField(widget=forms.TextInput)
     passward=forms.CharField(widget=forms.PasswordInput)
     confirm_passward=forms.CharField(widget=forms.PasswordInput)


     def clean(self):
         cleaned_data = super().clean()
         passward = cleaned_data['passward']
         confirm_passward = cleaned_data['confirm_passward']
         print(passward,confirm_passward)

         if passward != confirm_passward:
             raise forms.ValidationError("did not match passward")

    
  

        
             

