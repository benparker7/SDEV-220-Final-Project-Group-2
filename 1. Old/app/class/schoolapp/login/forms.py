from .util import list_entries

from django import forms


class SearchForm(forms.Form):
    """Search form."""

    keyword = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))
