from django import forms

class Contactform(forms.Form):
	fullname= forms.CharField(
			  widget=forms.TextInput(
	                  attrs={
	                  "class":"form-control",
	                  "placeholder":"Patient Name"
	                }      
		 	  	)

			)
	email   = forms.EmailField(
            widget=forms.EmailInput(
	                  attrs={
	                  "class":"form-control",
	                  "placeholder":"Patient Email"
	                }      
		 	  	)

			)
		
	content = forms.CharField(
		   widget=forms.Textarea(
             attrs={
             'class':'form-control',
             "placeholder":"Medicine (2-1-1)"
             }
		   	)


		)

	def clean_email(self):
		email=self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("email has to be gmail")
		return email 


	    
	    	 