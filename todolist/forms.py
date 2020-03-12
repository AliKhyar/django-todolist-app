from django import forms

class TodolistForm(forms.Form):
    """" """
    text = forms.CharField(max_length = 45, required = True,
    widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'type':'text',
            'placeholder':'Enter todo',
            'aria-describeby':'add-btn'
       }
   ),
       error_messages = {
           'required' : "This field is required",
           'invalid' : "This field is invalid",
   })

    def clean(self):
        cleaned_data = super().clean()
        #Do Stuff
