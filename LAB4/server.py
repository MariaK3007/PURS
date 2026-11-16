from flask import Flask, request, make_response, redirect, url_for, render_template

app = Flask(__name__)

temperatura = []

@app.get('/')
def home_page():
    return render_template('index.html'), 200

@app.get('/login')
def login_page():
    return render_template('login.html'), 200

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('home_page'))
    else:
        return redirect(url_for('login_page'))

@app.post('/temperatura')
def set_temperature():
    global temperatura
    response = make_response()

    if request.json.get('temperatura') is not None:
        temperatura.append(request.json.get('temperatura'))

        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201
    else:
        response.data = 'Niste napisali ispravan ključ'
        response.status_code = 404
    return response

@app.get('/temperatura')
def get_temepratura():
    json = { "temperatura": temperatura[-1] }
    response = make_response(json, 200)
    return response

@app.delete('/temperatura')
def delete_temperature():
    global temperatura

    response = make_response()

    if request.args.get('temperatura') is not None and int(request.args.get('id')) < len(temperatura):
        temperatura.remove(int(request.args.get('id')))
        response.data = 'Uspješno ste obrisali temepraturu'
        response.status_code = 202
    else:
        response.data = 'Upisali ste neispravan ključ'
        response.status_code = 404
    return response

if __name__=='__main__':
    app.run(host="0.0.0.0", port=80)