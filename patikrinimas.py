import unittest
from main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_patikrinimas()

    def test_kontaktai_form(self):
        response = self.app.post('/kontaktai', data=dict(vardas='Vardenis', pastas='vardas@pastas.lt', zinute='Žinutė'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Jūsų žinutė buvo sėkmingai išsiųsta.', response.data)

    def test_kontaktai_form_invalid(self):
        response = self.app.post('/kontaktai', data=dict(vardas='', pastas='', zinute=''), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti vardą', response.data)
        self.assertIn('*Prašome įvesti el. pašto adresą', response.data)
        self.assertIn('*Prašome įvesti žinutę', response.data)

    def test_kontaktai_form_invalid1(self):
        response = self.app.post('/kontaktai', data=dict(vardas='labas', pastas='labas@gmail.com', zinute=''),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti vardą', response.data)
        self.assertIn('*Prašome įvesti el. pašto adresą', response.data)
        self.assertIn('*Prašome įvesti žinutę', response.data)

    def test_kontaktai_form_invalid2(self):
        response = self.app.post('/kontaktai', data=dict(vardas='labas', pastas='', zinute=''), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti el. pašto adresą', response.data)
        self.assertIn('*Prašome įvesti žinutę', response.data)

    def test_kontaktai_form_invalid3(self):
        response = self.app.post('/kontaktai', data=dict(vardas='labas', pastas='', zinute='labas'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti el. pašto adresą', response.data)

    def test_kontaktai_form_invalid5(self):
        response = self.app.post('/kontaktai', data=dict(vardas='lab1234', pastas='labas@gmail.coom', zinute='labas'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Vardo laukelyje negali būti skaičių', response.data)

    def test_kontaktai_form_invalid6(self):
        response = self.app.post('/kontaktai', data=dict(vardas='lab/.', pastas='labas@gmail.com', zinute='labas'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Vardo laukelyje negali būti simbolių', response.data)

    def test_kontaktai_form_invalid7(self):
        response = self.app.post('/kontaktai', data=dict(vardas='labas', pastas='gmail@12', zinute='labas'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti teisingą el.pašto adresą', response.data)

    def test_kontaktai_form_invalid8(self):
        response = self.app.post('/kontaktai', data=dict(vardas='labas', pastas='gmail@gmail12', zinute='labas'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti teisingą el.pašto adresą', response.data)

    def test_kontaktai_form_invalid9(self):
        response = self.app.post('/kontaktai', data=dict(vardas='labas', pastas='gmail@12er.sf', zinute='labas'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('*Prašome įvesti teisingą el.pašto adresą', response.data)


if __name__ == '__main__':
    unittest.main()
