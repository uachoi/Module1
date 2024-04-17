from django import forms
from .models import Posting

class PostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title', 'content', 'image1', 'image2', 'image3']
        #widgets = {
        #    'image1': forms.ClearableFileInput(attrs={'onchange': 'validateFile()'}),
        #    'image2': forms.ClearableFileInput(attrs={'onchange': 'validateFile()'}),
        #    'image3': forms.ClearableFileInput(attrs={'onchange': 'validateFile()'}),
        #}
        
    def clean_image1(self):  # 파일 형식 추가
        image1 = self.cleaned_data.get('image1')
        if image1:
            extension = image1.name.rsplit('.', 1)[1].lower()
            if extension not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("JPG, JPEG, PNG 파일만 업로드 가능합니다.")
        return image1
    
    def clean_image2(self):  # 파일 형식 추가
        image2 = self.cleaned_data.get('image2')
        if image2:
            extension = image2.name.rsplit('.', 1)[1].lower()
            if extension not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("JPG, JPEG, PNG 파일만 업로드 가능합니다.")
        return image2
    
    def clean_image3(self):  # 파일 형식 추가
        image3 = self.cleaned_data.get('image3')
        if image3:
            extension = image3.name.rsplit('.', 1)[1].lower()
            if extension not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("JPG, JPEG, PNG 파일만 업로드 가능합니다.")
        return image3




class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
