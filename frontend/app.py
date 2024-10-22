from flask import Flask, render_template, request, send_file
from encryption import encrypt_data,generate_key, decrypt_data

app = Flask(__name__)

stored_value = ""

@app.route('/', methods=['GET', 'POST'])
def home():
    global stored_value
    if request.method == 'POST':
        stored_value = str(request.form['user_input'])
    return render_template('index.html', stored_value=stored_value)

@app.route('/submit', methods=['GET', 'POST'])
def get_encrypted():
    key = generate_key()
    with open('stored_value.txt', 'w') as f:
        f.write(str(key))
    encrypted_message = encrypt_data(stored_value, key)
    return render_template("encrypted.html", message = encrypted_message, key = key)

@app.route('/download')
def download_file():
    return send_file('stored_value.txt', as_attachment=True)

@app.route('/submit2', methods=['GET', 'POST'])
def get_decrypted():
    value = ""
    key = ""
    if request.method == 'POST':
        value = str(request.form['user_value'])
        key = request.form['user_key']
    decrypted =decrypt_data(value, key)
    print(decrypted)
    return render_template("decrypted.html", val = decrypted)


if __name__ == '__main__':
    app.run(debug=True)
