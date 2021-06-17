from django import forms


class QueryForm(forms.Form):
    user_search_term = forms.CharField(max_length=500, required=False)
    user_search_value = forms.CharField(max_length=500, required=False)
    org_search_term = forms.CharField(max_length=500, required=False)
    org_search_value = forms.CharField(max_length=500, required=False)
    tickets_search_term = forms.CharField(max_length=500, required=False)
    tickets_search_value = forms.CharField(max_length=500, required=False)
    user_search_per_key = forms.CharField(max_length=500, required=False)
    org_search_per_key = forms.CharField(max_length=500, required=False)
    tickets_search_per_key = forms.CharField(max_length=500, required=False)
    user_search_tag = forms.CharField(max_length=500, required=False)
    org_search_tag = forms.CharField(max_length=500, required=False)
    tickets_search_tag = forms.CharField(max_length=500, required=False)
    org_search_domain = forms.CharField(max_length=500, required=False)
