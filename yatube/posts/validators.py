from django import forms


def validate_not_empty(value):
    if not value:
        raise forms.ValidationError(
            'А кто поле будет заполнять, Пушкин?',
            params={'value': value},
        )
