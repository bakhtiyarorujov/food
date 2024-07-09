from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.forms import ContactForm


class ContanctViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        client = Client()
        cls.url = reverse_lazy('contact_us')
        cls.response = client.get(cls.url)
        cls.data = {
            'name': 'John',
            'email': 'johngmail.com',
            'subject': 'Test',
            'message': 'testmessage'
        }
        cls.post_invalid = client.post(cls.url, data=cls.data)
    
    def test_url(self):
        self.assertEqual(self.url, '/en/contact-us/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_response_context(self):
        self.assertIsInstance(self.response.context['form'], ContactForm)

    def test_form_errors(self):
        form = self.response.context['form']
        self.assertFalse(form.is_valid())

    @classmethod
    def tearDownClass(cls) -> None:
        pass