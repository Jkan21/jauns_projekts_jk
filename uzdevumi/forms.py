from django.forms import (
    Form,
    CharField,
    DateTimeField,
    EmailField,
    FileField,
)

class VisitForm(Form):
    visitor = CharField()
    date_time = DateTimeField()
    reason = CharField()


class CreateUserForm(Form):
    username = CharField()
    e_mail = EmailField()


class VisitorNameForm(Form):
    visitor_name = CharField()

class UploadCsvForm(Form):
    csv_file = FileField()