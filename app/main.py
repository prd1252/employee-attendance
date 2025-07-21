from flask import Flask, render_template

app = Flask(__name__)

# Sample employee data
employees = [
    {"id": "E001", "name": "Pushkaraj", "status": "Absent"},
    {"id": "E002", "name": "Chaitanya", "status": "Present"},
    {"id": "E003", "name": "Sachin", "status": "Present"},
    {"id": "E003", "name": "Mayur", "status": "Present"},
]

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')