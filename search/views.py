import distutils.util
from django.shortcuts import render
from search.forms import QueryForm
from search.main import SearchUsers, SearchOrganizations, SearchTickets


def searchpage(request):
    users_fields = SearchUsers().all_search_fields()
    orgs_fields = SearchOrganizations().all_search_fields()
    tickets_fields = SearchTickets().all_search_fields()
    users_tags = SearchUsers().alltags()
    orgs_tags = SearchOrganizations().alltags()
    tickets_tags = SearchTickets().alltags()
    orgs_domains = SearchOrganizations().alldomains()
    users_missing_values = SearchUsers().check_missing_values()
    orgs_missing_values = SearchOrganizations().check_missing_values()
    tickets_missing_values = SearchTickets().check_missing_values()

    if request.method == 'POST':
        def int_bool_conversion_attempt(str_inp):
            if str_inp == 'True' or str_inp == 'False':
                bool_conv = distutils.util.strtobool(str_inp)
                if bool_conv == 1:
                    return True
                else:
                    return False
            try:
                return int(str_inp)
            except TypeError:
                return str_inp
            except ValueError:
                return str_inp

        query_form = QueryForm(data=request.POST)
        if query_form.is_valid():
            user_key_search = query_form.cleaned_data['user_search_term']
            user_value_search = int_bool_conversion_attempt(query_form.cleaned_data['user_search_value'])
            org_key_search = query_form.cleaned_data['org_search_term']
            org_value_search = int_bool_conversion_attempt(query_form.cleaned_data['org_search_value'])
            tickets_key_search = query_form.cleaned_data['tickets_search_term']
            tickets_value_search = int_bool_conversion_attempt(query_form.cleaned_data['tickets_search_value'])
            user_search_per_key = query_form.cleaned_data['user_search_per_key']
            org_search_per_key = query_form.cleaned_data['org_search_per_key']
            tickets_search_per_key = query_form.cleaned_data['tickets_search_per_key']
            user_search_tag = int_bool_conversion_attempt(query_form.cleaned_data['user_search_tag'])
            org_search_tag = int_bool_conversion_attempt(query_form.cleaned_data['org_search_tag'])
            tickets_search_tag = int_bool_conversion_attempt(query_form.cleaned_data['tickets_search_tag'])
            org_search_domain = int_bool_conversion_attempt(query_form.cleaned_data['org_search_domain'])
            users_search_results = SearchUsers(key=user_key_search, value=user_value_search).searchresults()
            orgs_search_results = SearchOrganizations(key=org_key_search, value=org_value_search).searchresults()
            tickets_search_results = SearchTickets(key=tickets_key_search, value=tickets_value_search).searchresults()
            users_all_results_for_term = SearchUsers(key=user_search_per_key).all_values_for_key()
            orgs_all_results_for_term = SearchOrganizations(key=org_search_per_key).all_values_for_key()
            tickets_all_results_for_term = SearchTickets(key=tickets_search_per_key).all_values_for_key()
            users_results_per_tag = SearchUsers(value=user_search_tag).usersbytag()
            orgs_results_per_tag = SearchOrganizations(value=org_search_tag).organizationsbytag()
            tickets_results_per_tag = SearchTickets(value=tickets_search_tag).ticketsbytag()
            orgs_results_per_domain = SearchOrganizations(value=org_search_domain).organizationsbydomain()

            context = {'form_data': query_form,
                       'users_fields': users_fields,
                       'orgs_fields': orgs_fields,
                       'tickets_fields': tickets_fields,
                       'users_tags': users_tags,
                       'orgs_tags': orgs_tags,
                       'tickets_tags': tickets_tags,
                       'orgs_domains': orgs_domains,
                       'users_missing_values': users_missing_values,
                       'orgs_missing_values': orgs_missing_values,
                       'tickets_missing_values': tickets_missing_values,
                       'user_key_search': user_key_search,
                       'user_value_search': user_value_search,
                       'org_key_search': org_key_search,
                       'org_value_search': org_value_search,
                       'tickets_key_search': tickets_key_search,
                       'tickets_value_search': tickets_value_search,
                       'user_search_per_key': user_search_per_key,
                       'org_search_per_key': org_search_per_key,
                       'tickets_search_per_key': tickets_search_per_key,
                       'orgs_results_per_domain': orgs_results_per_domain,
                       'user_search_tag': user_search_tag,
                       'org_search_tag': org_search_tag,
                       'tickets_search_tag': tickets_search_tag,
                       'org_search_domain': org_search_domain,
                       'users_search_results': users_search_results,
                       'orgs_search_results': orgs_search_results,
                       'tickets_search_results': tickets_search_results,
                       'users_all_results_for_term': users_all_results_for_term,
                       'orgs_all_results_for_term': orgs_all_results_for_term,
                       'tickets_all_results_for_term': tickets_all_results_for_term,
                       'users_results_per_tag': users_results_per_tag,
                       'orgs_results_per_tag': orgs_results_per_tag,
                       'tickets_results_per_tag': tickets_results_per_tag,
                       }

            return render(request, 'searchpage.html', context)
        else:
            return render(request, 'searchpage.html')

    context = {'form': QueryForm(),
               'users_fields': users_fields,
               'orgs_fields': orgs_fields,
               'tickets_fields': tickets_fields,
               'users_tags': users_tags,
               'orgs_tags': orgs_tags,
               'tickets_tags': tickets_tags,
               'orgs_domains': orgs_domains,
               'users_missing_values': users_missing_values,
               'orgs_missing_values': orgs_missing_values,
               'tickets_missing_values': tickets_missing_values,
               }

    return render(request, 'searchpage.html', context)
