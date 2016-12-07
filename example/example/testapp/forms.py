import datetime

from django import forms
from django_calendar_field.forms import (
    CalendarMultipleChoiceField, CalendarRadioSelectMultiple,
)


class TestForm(forms.Form):
    calendar = CalendarMultipleChoiceField(
        label="Checkboxカレンダー",
        choices=(
            ('label1', "label1"),
            ('label2', "label2"),
            ('label3', "label3"),
        ),
        disables=(
            ('label1', [
                datetime.date.today(), datetime.date.today().replace(day=1)]),
            ('label3', [
                datetime.date.today().replace(day=10 + i) for i in range(10)])
        ),
        required=False
    )
    radio_calendar = CalendarMultipleChoiceField(
        label="RadioSelectカレンダー",
        choices=(
            ('label1', "label1"),
            ('label2', "label2"),
            ('label3', "label3"),
        ),
        disables=(
            ('label1', [
                datetime.date.today(), datetime.date.today().replace(day=1)]),
            ('label3', [
                datetime.date.today().replace(day=10 + i) for i in range(10)])
        ),
        required=False,
        widget=CalendarRadioSelectMultiple
    )
