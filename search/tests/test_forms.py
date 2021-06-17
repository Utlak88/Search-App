from django.test import TestCase
from search.forms import QueryForm


class QueryFormTest(TestCase):
    # def test_query_form_start_date_field_label(self):
    #     form = QueryForm()
    #     max_length = form.fields['user_search_term']].max_length
    #         'user_search_term'].label == 'user_search_term')

    # def test_query_form_start_date_initial_value(self):
    #     form = QueryForm()
    #     initial_value = form.fields['start_date'].initial['start_date']
    #     self.assertEqual(initial_value, '')
    #
    # def test_query_form_end_date_length(self):
    #     form = QueryForm()
    #     max_length = form.fields['end_date'].max_length
    #     self.assertEqual(max_length, 100)
    #
    # def test_query_form_end_date_initial_value(self):
    #     form = QueryForm()
    #     initial_value = form.fields['end_date'].initial['end_date']
    #     self.assertEqual(initial_value, '')
    #
    # def test_query_form_asset_length(self):
    #     form = QueryForm()
    #     max_length = form.fields['asset'].max_length
    #     self.assertEqual(max_length, 100)
    #
    # def test_query_form_asset_initial_value(self):
    #     form = QueryForm()
    #     initial_value = form.fields['asset'].initial['asset']
    #     self.assertEqual(initial_value, '')
    #
    # def test_query_form_asset_error_message(self):
    #     form = QueryForm()
    #     error_message = form.fields['asset'].error_messages['required']
    #     self.assertEqual(error_message, 'Error! Query(s) incorrectly entered. Please revise and try again.')
    #
    # # def test_query_form_column_field_label(self):
    # #     form = QueryForm()
    # #     max_length = form.fields['org_search_value'].max_length
    # #         'org_search_value'].label == 'org_search_value')
    #
    # def test_query_form_column_length(self):
    #     form = QueryForm()
    #     max_length = form.fields['column'].max_length
    #     self.assertEqual(max_length, 100)
    #
    # def test_query_form_column_initial_value(self):
    #     form = QueryForm()
    #     initial_value = form.fields['column'].initial['column']
    #     self.assertEqual(initial_value, '')
    #
    # def test_query_form_column_error_message(self):
    #     form = QueryForm()
    #     error_message = form.fields['column'].error_messages['required']
    #     self.assertEqual(error_message, 'Error! Query(s) incorrectly entered. Please revise and try again.')

    def test_query_form_correct_inputs(self):
        user_search_term = 'signature'
        user_search_value = 'Don\'t Worry Be Happy!'
        org_search_term = 'created_at'
        org_search_value = '2016-05-21T11:10:28 -10:00'
        tickets_search_term = 'created_at'
        tickets_search_value = '2016-04-28T11:19:34 -10:00'
        user_search_per_key = 'signature'
        org_search_per_key = 'created_at'
        tickets_search_per_key = 'created_at'
        user_search_tag = 'Balm'
        org_search_tag = 'Mclaughlin'
        tickets_search_tag = 'Iowa'
        org_search_domain = 'isoplex.com'
        form = QueryForm(data={
            'user_search_term': user_search_term,
            'user_search_value': user_search_value,
            'org_search_term': org_search_term,
            'org_search_value': org_search_value,
            'tickets_search_term': tickets_search_term,
            'tickets_search_value': tickets_search_value,
            'user_search_per_key': user_search_per_key,
            'org_search_per_key': org_search_per_key,
            'tickets_search_per_key': tickets_search_per_key,
            'user_search_tag': user_search_tag,
            'org_search_tag': org_search_tag,
            'tickets_search_tag': tickets_search_tag,
            'org_search_domain': org_search_domain})
        self.assertTrue(form.is_valid())

    def test_query_form_user_search_term_date_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['user_search_term'].label is None or form.fields[
            'user_search_term'].label == 'user_search_term')

    def test_query_form_user_search_value_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['user_search_value'].label is None or form.fields[
            'user_search_value'].label == 'user_search_value')

    def test_query_form_org_search_term_field_label(self):
        form = QueryForm()
        self.assertTrue(
            form.fields['org_search_term'].label is None or form.fields['org_search_term'].label == 'org_search_term')

    def test_query_form_org_search_value_field_label(self):
        form = QueryForm()
        self.assertTrue(
            form.fields['org_search_value'].label is None or form.fields[
                'org_search_value'].label == 'org_search_value')

    def test_query_form_tickets_search_term_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['tickets_search_term'].label is None or form.fields[
            'tickets_search_term'].label == 'tickets_search_term')

    def test_query_form_tickets_search_value_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['tickets_search_value'].label is None or form.fields[
            'tickets_search_value'].label == 'tickets_search_value')

    def test_query_form_user_search_per_key_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['user_search_per_key'].label is None or form.fields[
            'user_search_per_key'].label == 'user_search_per_key')

    def test_query_form_org_search_per_key_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['org_search_per_key'].label is None or form.fields[
            'org_search_per_key'].label == 'org_search_per_key')

    def test_query_form_tickets_search_per_key_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['tickets_search_per_key'].label is None or form.fields[
            'tickets_search_per_key'].label == 'tickets_search_per_key')

    def test_query_form_user_search_tag_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['user_search_tag'].label is None or form.fields[
            'user_search_tag'].label == 'user_search_tag')

    def test_query_form_org_search_tag_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['org_search_tag'].label is None or form.fields[
            'org_search_tag'].label == 'org_search_tag')

    def test_query_form_tickets_search_tag_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['tickets_search_tag'].label is None or form.fields[
            'tickets_search_tag'].label == 'tickets_search_tag')

    def test_query_form_org_search_domain_field_label(self):
        form = QueryForm()
        self.assertTrue(form.fields['org_search_domain'].label is None or form.fields[
            'org_search_domain'].label == 'org_search_domain')

    def test_query_form_user_search_term_date_max_length(self):
        form = QueryForm()
        max_length = form.fields['user_search_term'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_user_search_value_max_length(self):
        form = QueryForm()
        max_length = form.fields['user_search_value'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_org_search_term_max_length(self):
        form = QueryForm()
        max_length = form.fields['org_search_term'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_org_search_value_max_length(self):
        form = QueryForm()
        max_length = form.fields['org_search_value'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_tickets_search_term_max_length(self):
        form = QueryForm()
        max_length = form.fields['tickets_search_term'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_tickets_search_value_max_length(self):
        form = QueryForm()
        max_length = form.fields['tickets_search_value'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_user_search_per_key_max_length(self):
        form = QueryForm()
        max_length = form.fields['user_search_per_key'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_org_search_per_key_max_length(self):
        form = QueryForm()
        max_length = form.fields['org_search_per_key'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_tickets_search_per_key_max_length(self):
        form = QueryForm()
        max_length = form.fields['tickets_search_per_key'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_user_search_tag_max_length(self):
        form = QueryForm()
        max_length = form.fields['user_search_tag'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_org_search_tag_max_length(self):
        form = QueryForm()
        max_length = form.fields['org_search_tag'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_tickets_search_tag_max_length(self):
        form = QueryForm()
        max_length = form.fields['tickets_search_tag'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_org_search_domain_max_length(self):
        form = QueryForm()
        max_length = form.fields['org_search_domain'].max_length
        self.assertEqual(max_length, 500)

    def test_query_form_user_search_term_date_required(self):
        form = QueryForm()
        required = form.fields['user_search_term'].required
        self.assertEqual(required, False)

    def test_query_form_user_search_value_required(self):
        form = QueryForm()
        required = form.fields['user_search_value'].required
        self.assertEqual(required, False)

    def test_query_form_org_search_term_required(self):
        form = QueryForm()
        required = form.fields['org_search_term'].required
        self.assertEqual(required, False)

    def test_query_form_org_search_value_required(self):
        form = QueryForm()
        required = form.fields['org_search_value'].required
        self.assertEqual(required, False)

    def test_query_form_tickets_search_term_required(self):
        form = QueryForm()
        required = form.fields['tickets_search_term'].required
        self.assertEqual(required, False)

    def test_query_form_tickets_search_value_required(self):
        form = QueryForm()
        required = form.fields['tickets_search_value'].required
        self.assertEqual(required, False)

    def test_query_form_user_search_per_key_required(self):
        form = QueryForm()
        required = form.fields['user_search_per_key'].required
        self.assertEqual(required, False)

    def test_query_form_org_search_per_key_required(self):
        form = QueryForm()
        required = form.fields['org_search_per_key'].required
        self.assertEqual(required, False)

    def test_query_form_tickets_search_per_key_required(self):
        form = QueryForm()
        required = form.fields['tickets_search_per_key'].required
        self.assertEqual(required, False)

    def test_query_form_user_search_tag_required(self):
        form = QueryForm()
        required = form.fields['user_search_tag'].required
        self.assertEqual(required, False)

    def test_query_form_org_search_tag_required(self):
        form = QueryForm()
        required = form.fields['org_search_tag'].required
        self.assertEqual(required, False)

    def test_query_form_tickets_search_tag_required(self):
        form = QueryForm()
        required = form.fields['tickets_search_tag'].required
        self.assertEqual(required, False)

    def test_query_form_org_search_domain_required(self):
        form = QueryForm()
        required = form.fields['org_search_domain'].required
        self.assertEqual(required, False)
