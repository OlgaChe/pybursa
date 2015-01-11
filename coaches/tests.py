from django.test import TestCase


class CoachTests(TestCase):
    def test_coach_create(self):
        coach1 = Coach.objects.create(
        name='Severus',
        surname='Snape')
        self.assertEqual(Coach.objects.all().count(), 1)

    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/coach/')
        self.assertEqual(response.status_code, 200)
        coach1 = Coach.objects.create(name='Severus', surname='Snape')
        response = client.get('/coach/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Severus")


