from django import forms


class SingleEventDistributionSiteDetailForm(forms.Form):
    event_distribution_site_details = forms.IntegerField(required=True)
