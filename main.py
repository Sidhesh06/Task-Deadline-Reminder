from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import datetime

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Configure email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password
mail = Mail(app)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(
        title=data['title'],
        deadline=datetime.datetime.strptime(data['deadline'], '%Y-%m-%d %H:%M:%S'),
        email=data['email']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully!'})

@app.route('/send_reminders', methods=['GET'])
def send_reminders():
    tasks = Task.query.all()
    now = datetime.datetime.now()
    for task in tasks:
        if 0 < (task.deadline - now).total_seconds() < 3600:  # Reminder 1 hour before deadline
            msg = Message('Task Deadline Reminder',
                          sender='your-email@gmail.com',
                          recipients=[task.email])
            msg.body = f"Reminder: Your task '{task.title}' is due at {task.deadline}."
            mail.send(msg)
    return jsonify({'message': 'Reminders sent!'})

if __name__ == '__main__':
    app.run(debug=True)
