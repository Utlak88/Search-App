import unittest
from search.main import SearchUsers, SearchOrganizations, SearchTickets
from django.test import Client


class SearchApp(unittest.TestCase):
    """Runs 21 tests to validate that the search app is functioning correctly."""

    def setUp(self):
        """Establishing client that will be used to issue POST requests."""
        self.client = Client()

    def test_UserSearchTerms_ExpectedOutput(self):
        """Testing that all user available search terms are correctly output in app."""

        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchUsers().all_search_fields(),
                         test_response.context[-1]['users_fields'])

    def test_OrgSearchTerms_ExpectedOutput(self):
        """Testing that all organization available search terms are correctly output in app."""

        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations().all_search_fields(),
                         test_response.context[-1]['orgs_fields'])

    def test_TicketsSearchTerms_ExpectedOutput(self):
        """Testing that all ticket available search terms are correctly output in app."""

        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchTickets().all_search_fields(),
                         test_response.context[-1]['tickets_fields'])

    def test_UserMissingValues_ExpectedOutput(self):
        """Testing that all user missing values are correctly output in app."""

        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchUsers().check_missing_values(),
                         test_response.context[-1]['users_missing_values'])

    def test_OrgMissingValues_ExpectedOutput(self):
        """Testing that all organization missing values are correctly output in app."""

        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations().check_missing_values(),
                         test_response.context[-1]['orgs_missing_values'])

    def test_TicketsMissingValues_ExpectedOutput(self):
        """Testing that all ticket missing values are correctly output in app."""
        
        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchTickets().check_missing_values(),
                         test_response.context[-1]['tickets_missing_values'])

    def test_UserAllTags_ExpectedOutput(self):
        """Testing that all user tags are correctly output in app."""
        
        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchUsers().alltags(),
                         test_response.context[-1]['users_tags'])

    def test_OrgAllTags_ExpectedOutput(self):
        """Testing that all organization tags are correctly output in app."""
        
        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations().alltags(),
                         test_response.context[-1]['orgs_tags'])

    def test_TicketsAllTags_ExpectedOutput(self):
        """Testing that all ticket tags are correctly output in app."""

        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchTickets().alltags(),
                         test_response.context[-1]['tickets_tags'])

    def test_OrgAllDomains_ExpectedOutput(self):
        """Testing that all organization domain names are correctly output in app."""
       
        # Retrieving client POST data
        test_response = self.client.post('')

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations().alldomains(),
                         test_response.context[-1]['orgs_domains'])

    def test_HTTP_OK_response(self):
        # Retrieving client POST data for specified form fields   
        test_response = self.client.post('', {'user_search_term': '_id',
                                              'user_search_value': 1})

        # Validating HTTP 200 success response code
        self.assertEqual(test_response.status_code, 200)

    def test_UserSearchPOST_request(self):
        """Testing that user search results are correctly output in app."""
        
        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'user_search_term': '_id',
                                               'user_search_value': 1})

        # Validating app outputs correct response
        self.assertEqual(SearchUsers(key='_id', value=1).searchresults(),
                         test_response1.context[-1]['users_search_results'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'user_search_term': '_id1',
                                               'user_search_value': '1'})

        # Validating app outputs correct response
        self.assertEqual(SearchUsers(key='_id1', value='1').searchresults(),
                         test_response2.context[-1]['users_search_results'])

    def test_OrgSearchPOST_request(self):
        """Testing that organzation search results are correctly output in app."""
        
        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'org_search_term': '_id',
                                               'org_search_value': 101})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(key='_id', value=101).searchresults(),
                         test_response1.context[-1]['orgs_search_results'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'org_search_term': '_id1',
                                               'org_search_value': '101'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(key='_id1', value='101').searchresults(),
                         test_response2.context[-1]['orgs_search_results'])

    def test_TicketSearchPOST_request(self):
        """Testing that ticket search results are correctly output in app."""
        
        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'tickets_search_term': '_id',
                                               'tickets_search_value': '436bf9b0-1147-4c0a-8439-6f79833bff5b'})

        # Validating app outputs correct response
        self.assertEqual(
            SearchTickets(key='_id', value='436bf9b0-1147-4c0a-8439-6f79833bff5b').searchresults(),
            test_response1.context[-1]['tickets_search_results'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'tickets_search_term': '_id1',
                                               'tickets_search_value': 'a436bf9b0-1147-4c0a-8439-6f79833bff5b'})

        # Validating app outputs correct response
        self.assertEqual(SearchTickets(key='_id1', value='a436bf9b0-1147-4c0a-8439-6f79833bff5b').searchresults(),
                         test_response2.context[-1]['tickets_search_results'])

    def test_UserResultsPerTermPOST_request(self):
        """Testing that user search values for a search term are correctly output in app."""
        
        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'user_search_per_key': '_id'})

        # Validating app outputs correct response
        self.assertEqual(SearchUsers(key='_id').all_values_for_key(),
                         test_response1.context[-1]['users_all_results_for_term'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'user_search_per_key': '_id1'})

        # Validating app outputs correct response
        self.assertEqual(SearchUsers(key='_id1').all_values_for_key(),
                         test_response2.context[-1]['users_all_results_for_term'])

    def test_OrgResultsPerTermPOST_request(self):
        """Testing that organization search values for a search term are correctly output in app."""

        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'org_search_per_key': '_id'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(key='_id').all_values_for_key(),
                         test_response1.context[-1]['orgs_all_results_for_term'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'org_search_per_key': '_id1'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(key='_id1').all_values_for_key(),
                         test_response2.context[-1]['orgs_all_results_for_term'])

    def test_TicketResultsPerTermPOST_request(self):
        """Testing that ticket search values for a search term are correctly output in app."""

        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'tickets_search_per_key': '_id'})

        # Validating app outputs correct response
        self.assertEqual(SearchTickets(key='_id').all_values_for_key(),
                         test_response1.context[-1]['tickets_all_results_for_term'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'tickets_search_per_key': '_id1'})

        # Validating app outputs correct response
        self.assertEqual(SearchTickets(key='_id1').all_values_for_key(),
                         test_response2.context[-1]['tickets_all_results_for_term'])

    def test_UserResultsPerTagPOST_request(self):
        """Testing that user search values for a tag are correctly output in app."""

        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'user_search_tag': 'Riverton'})

        # Validating app outputs correct response
        self.assertEqual(SearchUsers(value='Riverton').usersbytag(),
                         test_response1.context[-1]['users_results_per_tag'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'user_search_tag': '1Riverton'})

        # Validating app outputs correct response
        self.assertEqual(SearchUsers(value='1Riverton').usersbytag(),
                         test_response2.context[-1]['users_results_per_tag'])

    def test_OrgResultsPerTagPOST_request(self):
        """Testing that organization search values for a tag are correctly output in app."""

        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'org_search_tag': 'Maddox'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(value='Maddox').organizationsbytag(),
                         test_response1.context[-1]['orgs_results_per_tag'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'org_search_tag': '1Maddox'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(value='1Maddox').organizationsbytag(),
                         test_response2.context[-1]['orgs_results_per_tag'])

    def test_TicketResultsPerTagPOST_request(self):
        """Testing that ticket search values for a tag are correctly output in app."""

        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'tickets_search_tag': 'Northern Mariana Islands'})

        # Validating app outputs correct response
        self.assertEqual(SearchTickets(value='Northern Mariana Islands').ticketsbytag(),
                         test_response1.context[-1]['tickets_results_per_tag'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'tickets_search_tag': '1Northern Mariana Islands'})

        # Validating app outputs correct response
        self.assertEqual(SearchTickets(value='1Northern Mariana Islands').ticketsbytag(),
                         test_response2.context[-1]['tickets_results_per_tag'])

    def test_OrgResultsPerDomainPOST_request(self):
        """Testing that organization search values for a domain name are correctly output in app."""

        # Retrieving client POST data for correct form fields
        test_response1 = self.client.post('', {'org_search_domain': 'quantasis.com'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(value='quantasis.com').organizationsbydomain(),
                         test_response1.context[-1]['orgs_results_per_domain'])

        # Retrieving client POST data for incorrect form fields
        test_response2 = self.client.post('', {'org_search_domain': '1quantasis.com'})

        # Validating app outputs correct response
        self.assertEqual(SearchOrganizations(value='1quantasis.com').organizationsbydomain(),
                         test_response2.context[-1]['orgs_results_per_domain'])


if __name__ == '__main__':
    # Runs all unit tests
    unittest.main()
