from flask import Flask, render_template_string, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'postgres')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'testdb')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


# HTML Template
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
<title>User Registration</title>

<style>

body{
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#667eea,#764ba2);
    margin:0;
    padding:0;
}

.container{
    max-width:700px;
    margin:60px auto;
    background:white;
    padding:30px;
    border-radius:10px;
    box-shadow:0 10px 25px rgba(0,0,0,0.2);
}

h1{
    text-align:center;
    color:#333;
}

form{
    text-align:center;
    margin-bottom:30px;
}

input{
    width:80%;
    padding:12px;
    margin:8px 0;
    border-radius:6px;
    border:1px solid #ccc;
    font-size:14px;
}

input:focus{
    border-color:#667eea;
    outline:none;
}

button{
    background:#667eea;
    color:white;
    border:none;
    padding:12px 25px;
    border-radius:6px;
    font-size:16px;
    cursor:pointer;
}

button:hover{
    background:#5a67d8;
}

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#667eea;
    color:white;
    padding:10px;
}

td{
    padding:10px;
    text-align:center;
    border-bottom:1px solid #eee;
}

tr:hover{
    background:#f5f5f5;
}

.count{
    text-align:center;
    margin-bottom:10px;
    font-weight:bold;
}

</style>

</head>

<body>

<div class="container">

<h1>User Registration</h1>

<form method="POST">
<input type="text" name="name" placeholder="Enter your name" required>
<br>
<input type="email" name="email" placeholder="Enter your email" required>
<br>
<button type="submit">Register</button>
</form>

<div class="count">Total Users: {{ users|length }}</div>

<table>

<tr>
<th>ID</th>
<th>Name</th>
<th>Email</th>
</tr>

{% for user in users %}
<tr>
<td>{{ user.id }}</td>
<td>{{ user.name }}</td>
<td>{{ user.email }}</td>
</tr>
{% endfor %}

</table>

</div>

</body>
</html>
'''


# Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email']
        )

        db.session.add(user)
        db.session.commit()

        return redirect('/')

    users = User.query.all()
    return render_template_string(TEMPLATE, users=users)


# Create tables
with app.app_context():
    db.create_all()
    print("✓ Database tables created")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)