from django.forms import Form, CharField, EmailField

class Users(Form):

    user = CharField()
    email = EmailField()
