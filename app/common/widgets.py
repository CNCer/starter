from django import forms
from django.forms.widgets import Select
from django.utils.html import format_html

class DisableOptionSelect(Select):
    def render_option(self, selected_choices, option_value, option_label):
        if option_value in self.disabled_choices:
            return format_html('<option value="{}" disabled>{}</option>', option_value, option_label)
        return super().render_option(selected_choices, option_value, option_label)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if value in self.disabled_choices:
            option['attrs']['disabled'] = True
        return option

    def __init__(self, *args, disabled_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.disabled_choices = disabled_choices or []

