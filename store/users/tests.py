from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    fixtures = ['socialapp.json']

    def setUp(self):
        self.path = reverse('users:registration')
        self.form_data = {
            'first_name': 'Vladimir',
            'last_name': 'Trofimenko',
            'username': 'bibo85',
            'email': 'psdmaster.ru@gmail.com',
            'password1': '12345678pP',
            'password2': '12345678pP',
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация пользователя')
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertIsInstance(response.context_data['form'], UserRegistrationForm)

    def test_user_registration_post_success(self):
        username = self.form_data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.form_data)

        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # check creating of email verification
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        User.objects.create(username=self.form_data['username'])

        response = self.client.post(self.path, self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)


class UserLoginViewTestCase(TestCase):
    fixtures = ['socialapp.json']

    def setUp(self):
        self.user_data = {
            'username': 'TestUser',
            'email': 'test@test.ru',
            'password': 'testpassword',
        }
        self.login_url = reverse('users:login')
        self.user = User.objects.create_user(**self.user_data)

    def test_login_page_loads_successfully(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertEqual(response.context_data['title'], 'Store - Авторизация')
        self.assertIsInstance(response.context_data['form'], UserLoginForm)

    def test_login_successful(self):
        response = self.client.post(self.login_url, self.user_data)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(self.client.session['_auth_user_id'])

    def test_login_failure(self):
        data = {
            'username': self.user_data['username'],
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertTrue(response.context_data['form'].errors)
        self.assertIsInstance(response.context_data['form'], UserLoginForm)
        self.assertContains(response, 'Пожалуйста, введите правильные имя пользователя и пароль. '
                                      'Оба поля могут быть чувствительны к регистру.', html=True)
