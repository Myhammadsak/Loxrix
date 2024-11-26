from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class ProjectViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.project1 = Project.objects.create(name="Project 1", creator=self.user)
        self.project2 = Project.objects.create(name="Project 2", creator=self.user)

    def test_list_projects(self):
        response = self.client.get('/api/v1/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_projects_by_created_at(self):
        response = self.client.get('/api/v1/projects/', {'created_at__gte': self.project1.created_at})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_ordering_projects_by_name(self):
        response = self.client.get('/api/v1/projects/', {'ordering': 'name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Project 1')

    def test_delete_project(self):
        response = self.client.delete(f'/api/v1/projects/{self.project1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(id=self.project1.id).exists())