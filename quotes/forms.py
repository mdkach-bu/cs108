#quotes/forms.py

from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    """A form to add new quotes to the database."""

    class Meta:
        """Associate this form with the Quote mode."""
        model = Quote
        fields = ['person', 'text', ] #which fields from model should we use

class UpdateQuoteForm(forms.ModelForm):
    """A form to update a quote to the database."""

    class Meta:
        """Associate this form with the Quote mode."""
        model = Quote
        fields = ['person', 'text', ] #which fields from model should we use 


