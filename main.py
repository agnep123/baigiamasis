from flask import Flask, render_template, request
import re
import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'sveiki'  # sekretinis raktas skirtas flash funkcijai


@app.route('/layouts')
def layout():
    return render_template('layouts.html')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/apie_mus')
def apie_mus():
    return render_template('apiemus.html')


@app.route('/keliones')
def keliones():
    return render_template('keliones.html')


@app.route('/kontaktai')
def kontaktai():
    return render_template('kontaktai.html')


is_testing = True


@app.route('/kontaktai', methods=['GET', 'POST'])
def handle_kontaktai_form():
    if request.method == 'POST':
        try:
            vardas = request.form['vardas']
            pastas = request.form['pastas']
            zinute = request.form['zinute']

            errors = {}
            if not vardas:
                errors['vardas'] = '*Prašome įvesti vardą'
            if not pastas:
                errors['pastas'] = '*Prašome įvesti el. pašto adresą'
            elif not re.match(r'^\S+@\S+\.\S+$', pastas):
                errors['pastas'] = '*El. pašto adresas yra neteisingas'
            if not zinute:
                errors['zinute'] = '*Prašome įvesti žinutę'

            if errors:
                return render_template('kontaktai.html', errors=errors)
            else:
                if not is_testing:
                    # išsaugojame formos duomenis į tekstinį failą
                    with open('formos_duomenys.txt', 'a', encoding='utf-8') as f:
                        f.write(f'Įrašymo data: {datetime.datetime.now()}\n\n')
                        f.write(f'Vardas: {vardas}\n')
                        f.write(f'El. paštas: {pastas}\n')
                        f.write(f'Žinutė: {zinute}\n')

                sekmingai_issiusta = True
                return render_template('kontaktai.html', sekmingai_issiusta=sekmingai_issiusta)
        except Exception as e:
            error_message = str(e)
            return render_template('kontaktai.html', error_message=error_message)
    else:
        return render_template('kontaktai.html')


if __name__ == "__main__":
    app.run(debug=True)
