from django.test import TestCase


class CourseTests(TestCase):
    def test_course_create(self):
        course1 = Course.objects.create(
        name='Python',
        start_date=date(2014, 10, 10))
        self.assertEqual(Course.objects.all().count(), 1)

    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        course1 = Course.objects.create(name='Python', start_date=date(2014, 10, 10))
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")


