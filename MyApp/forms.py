from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')   # CharField: Поле для текстовых данных.
    email = forms.EmailField(label='Your email')   # EmailField: Поле для электронной почты (встроенная проверка на корректность).
    message = forms.CharField(widget=forms.Textarea, label='Message')   # widget=forms.Textarea: Позволяет отобразить большое текстовое поле.

