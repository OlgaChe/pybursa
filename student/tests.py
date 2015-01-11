from django.test import TestCase


class StudentTests(TestCase):
    def test_student_create(self):
        student1 = Student.objects.create(
        name='Draco',
        surname='Malfloy')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/student/')
        self.assertEqual(response.status_code, 200)
        student1 = Student.objects.create(name='Draco', surname='Malfloy')
        response = client.get('/student/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Draco")


