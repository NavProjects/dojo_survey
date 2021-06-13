from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'keeping this safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['city_chosen'] = request.form['city']
    session['language_chosen'] = request.form.getlist('language')
    session['comment_put'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def new():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)