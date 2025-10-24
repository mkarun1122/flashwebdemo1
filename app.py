from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Route for registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Here you could add logic to save user info (e.g., to a database)
        # For this example, we’ll just redirect to the success page.
        return redirect(url_for('successful', username=username))

    return render_template('register.html')


# Route for success page
@app.route('/successful')
def successful():
    username = request.args.get('username', 'User')
    return render_template('successful.html', username=username)


if __name__ == '__main__':
    app.run(debug=True,port=3002)
