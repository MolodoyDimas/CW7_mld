from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = '/users/user/'
        self.data = {
            'email': 'test@test.ru',
            'password': 'test',
            'telegram': '@test',
            'chat_id': 12345
        }

    def test_create_user(self):
        """Тестирование создание пользователя"""

        response = self.client.post(f'{self.url}', data=self.data)

        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {
                'id': 7,
                'email': 'test@test.ru',
                'password': 'test',
                'telegram': '@test',
                'chat_id': 12345
            }
        )
