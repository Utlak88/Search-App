from django.test import TestCase
from django.urls import reverse
# from django.test.utils import setup_test_environment
#
# setup_test_environment()
from django.test import Client

client = Client()


class SearchpageViewTest(TestCase):
    def test_searchpage_url_exists_at_desired_location(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)

    def test_searchpage_url_accessible_by_name(self):
        response = self.client.post(reverse('searchpage'))
        self.assertEqual(response.status_code, 200)

    def test_searchpage_uses_correct_template(self):
        response = self.client.post(reverse('searchpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchpage.html')

    def test_searchpage_correct_user_search_term_value_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'user_search_term': 'signature',
                                                            'user_search_value': 'Don\'t Worry Be Happy!',
                                                            })
        self.assertIn('74341f74-9c79-49d5-9611-87ef9b6eb75f', response.content.decode())

    def test_searchpage_correct_org_search_term_value_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'org_search_term': 'url',
                                                            'org_search_value': 'http://tech.orangeshine.com/api/v2/organizations/101.json',
                                                            })
        self.assertIn('9270ed79-35eb-4a38-a46f-35725197ea8d', response.content.decode())

    def test_searchpage_correct_ticket_search_term_value_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'tickets_search_term': 'description',
                                                            'tickets_search_value': 'Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.',
                                                            })
        self.assertIn('436bf9b0-1147-4c0a-8439-6f79833bff5b', response.content.decode())

    def test_searchpage_correct_user_search_per_key_jsonresponse(self):
        response = self.client.post(reverse('searchpage'),
                                    {'user_search_per_key': 'signature'})
        self.assertIn('Don&#x27;t Worry Be Happy!', response.content.decode())

    def test_searchpage_correct_org_search_per_key_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'org_search_per_key': 'name'})
        self.assertIn('Enthaze', response.content.decode())

    def test_searchpage_correct_tickets_search_per_key_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'tickets_search_per_key': 'priority'})
        self.assertIn('high', response.content.decode())

    def test_searchpage_correct_user_search_tag_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'user_search_tag': 'Balm'})
        self.assertIn('Watkins Hammond', response.content.decode())

    def test_searchpage_correct_org_search_tag_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'org_search_tag': 'Bartlett'})
        self.assertIn('Speedbolt', response.content.decode())

    def test_searchpage_correct_tickets_search_tag_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'tickets_search_tag': 'Michigan'})
        self.assertIn('0a8d9bab-b265-4801-8d64-ba6cba3df967', response.content.decode())

    def test_searchpage_correct_org_search_domain_jsonresponse(self):
        response = self.client.post(reverse('searchpage'), {'org_search_domain': 'elemantra.com'})
        self.assertIn('be72663b-338d-42f4-bd52-cf6584cad674', response.content.decode())
