from django import forms


class ThumbnailComparisonForm(forms.Form):
    winner = forms.CharField(widget=forms.HiddenInput())
    loser = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        winner = cleaned_data.get('winner')
        loser = cleaned_data.get('loser')

        if not winner or not loser:
            raise forms.ValidationError("Both winner and loser fields are required.")

        if winner == loser:
            raise forms.ValidationError("Winner and loser cannot be the same.")

        return cleaned_data