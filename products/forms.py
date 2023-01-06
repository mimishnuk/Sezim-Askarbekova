from django import forms


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    price = forms.IntegerField()
    discription = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(max_value=10)
    commentable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'check': True}))

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=3, label='Your review')

