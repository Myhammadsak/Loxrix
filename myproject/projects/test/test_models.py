from django.test import TestCase
from projects.models import Project
from users.models import User


class AuthorModelTest(TestCase):

    def setUp(self):

        self.creator = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project.",
            status="active",
            creator=self.creator
        )

    def test_name_length(self):
        author=Project.objects.get(id=1)
        length = author._meta.get_field('name').max_length
        self.assertEqual(length,255)

    def test_description_blank(self):
        author=Project.objects.get(id=1)
        field_label = author._meta.get_field('description').blank
        self.assertEqual(field_label,True)

    def test_description_null(self):
        author=Project.objects.get(id=1)
        nul = author._meta.get_field('description').null
        self.assertEqual(nul,True)

    def test_status_length(self):
        author=Project.objects.get(id=1)
        length = author._meta.get_field('status').max_length
        self.assertEqual(length,20)

    def test_users_name(self):
        author=Project.objects.get(id=1)
        related_name = author._meta.get_field('users')._related_name
        self.assertEqual(related_name, 'projects')

    def test_creator_null(self):
        author=Project.objects.get(id=1)
        null = author._meta.get_field('creator').null
        self.assertEqual(null, True)

    def test_creator_blank(self):
        author=Project.objects.get(id=1)
        blank = author._meta.get_field('creator').blank
        self.assertEqual(blank, True)

    def test_creator_name(self):
        author=Project.objects.get(id=1)
        name = author._meta.get_field('creator')._related_name
        self.assertEqual(name, 'created_projects')

    def test_creaffffted_at(self):
        author=Project.objects.get(id=1)
        add = author._meta.get_field('created_at').auto_now_add
        self.assertEqual(add, True)

    def test_updated_at(self):
        author=Project.objects.get(id=1)
        now = author._meta.get_field('updated_at').auto_now
        self.assertEqual(now, True)

    def test_project_str(self):
        self.assertEqual(str(self.project), self.project.name)