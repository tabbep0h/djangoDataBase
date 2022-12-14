from django import forms

class CreatePostsForm(forms.Form):
    CHOICES = (("Наука","Наука"),('Юмор','Юмор'),('Блог','Блог'),('Путешествие','Путешествие'))
    name = forms.CharField(min_length=4,widget = forms.TextInput(attrs = {"class":"name__input input","placeholder":"Введите Заголовок"}), required =True,label = "Заголовок")
    url = forms.URLField(min_length=6,widget = forms.TextInput(attrs={"class":"url__input input","placeholder":"Введите адрес"}),required=True,label="URL")
    content = forms.CharField(min_length=6,widget = forms.Textarea(attrs={"class":"content__input input"}),required=True,label="Контент")
    published = forms.BooleanField(widget = forms.CheckboxInput(attrs={"class":"check__input input"}),required=True,label="Публикация")
    category = forms.ChoiceField(choices=CHOICES,widget = forms.Select(attrs={"class":"select__input input"}),required=True,label="Категории")


