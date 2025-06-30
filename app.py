from flask import Flask, render_template
app = Flask(__name__) # Corrected: __name_

@app.route('/')
def index():
    return render_template('index.html')  # Loads your HTML page

if __name__ == '__main__':  # Corrected: __main_
    app.run(debug=True)