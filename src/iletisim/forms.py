from django import forms
from .models import Contact,Teklif


class ContactForm(forms.ModelForm):
    gizlilik_sözleşmesi = forms.BooleanField()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message','subject','phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad, Soyad'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Konu'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Numarası'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Posta'}),
            # 'gizlilik': forms.BooleanField(attrs={'placeholder': 'Kabul Ediyorum,'}),
            # 'subject': forms.ChoiceField(attrs={'placeholder': 'Talebiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesaj'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'





UYER = (
    ('instagram', 'İnstagram'),
    ('twitter', 'Twitter'),
    ('facebook', 'Facebook'),
)
class TeklifForm(forms.ModelForm):
    gizlilik_sözleşmesi = forms.BooleanField()
    class Meta:
        model = Teklif
        fields = ['name', 'email', 'message','phone','hizmet','sehir','ilce','u_yer',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad, Soyad'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Konu'}),
            'hizmet': forms.TextInput(attrs={'placeholder': 'Hizmet Adı'}),
            'ilce': forms.TextInput(attrs={'placeholder': 'İlçe'}),
            'sehir': forms.TextInput(attrs={'placeholder': 'Şehir'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Numarası'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Posta'}),            
            'u_yer': forms.Select(choices=UYER,attrs={'class': 'form-control'}),

            # 'gizlilik': forms.BooleanField(attrs={'placeholder': 'Kabul Ediyorum,'}),
            # 'subject': forms.ChoiceField(attrs={'placeholder': 'Talebiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesaj'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'

