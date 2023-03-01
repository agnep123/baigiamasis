import unittest
from main import handle_kontaktai_form, app


class TestHandleKontaktaiForm(unittest.TestCase):

    def test_kontaktai(self):
        tester = app.test_client(self)
        response = tester.get('/kontaktai', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Kontaktai' in response.data)

    def test_invalid_vardas(self):
        with self.assertRaises(ValueError):
            handle_kontaktai_form("1234")  # vardas netinka - turi būti tik raidės

    def test_valid_vardas(self):
        # Patikriname, kad funkcija negeneruoja jokios išimties ir grąžina teisingą reikšmę
        result = handle_kontaktai_form("Jonas")
        self.assertEqual(result, None)

        # Patikriname, kad funkcija negeneruoja jokios išimties ir grąžina teisingą reikšmę
        result = handle_kontaktai_form("Petras")
        self.assertEqual(result, None)

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError):
            handle_kontaktai_form("Jonas", "invalid_email", "Test message")

    def test_valid_email_format(self):
        result = handle_kontaktai_form("Jonas", "valid_email@example.com", "Test message")
        self.assertEqual(result, None)

    def test_empty_message(self):
        with self.assertRaises(ValueError):
            handle_kontaktai_form("Jonas", "valid_email@example.com", "")

    def test_empty_email(self):
        with self.assertRaises(ValueError):
            handle_kontaktai_form("Jonas", "", "Test message")

    def test_long_message(self):
        with self.assertRaises(ValueError):
            handle_kontaktai_form("Jonas", "valid_email@example.com", "a" * 1001)


if __name__ == '__main__':
    unittest.main()
