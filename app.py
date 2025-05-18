from flask import Flask, render_template
from flask import request, flash, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Format the message
        entry = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}\n{'-'*40}\n"

        # Define the file path
        file_path = os.path.join(os.getcwd(), 'messages.txt')

        try:
            # Append the message to the file
            with open(file_path, 'a') as f:
                f.write(entry)
        except Exception as e:
            print(f"Failed to write message: {e}")
            flash("Oops! Something went wrong. Please try again.", "error")
            return redirect('/contact')

        flash("Thanks for your message! I'll get back to you soon.", "success")
        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
