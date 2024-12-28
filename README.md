# Task Deadline Reminder

## Project Description
Task Deadline Reminder is a simple MicroSaaS tool to help users stay on top of their tasks. It allows users to add tasks with deadlines and sends email reminders one hour before the deadline.

## Features
- Add tasks with a title, deadline, and email address.
- Sends email reminders before the task deadline.
- Simple and user-friendly API.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task-deadline-reminder

2. Install dependencies:
   pip install -r requirements.txt

3. Set up email configuration:
   Open main.py.
   Replace your-email@gmail.com and your-email-password with your email credentials.

4. Run the application:
   python main.py

5. Use Postman to interact with the application.

# Task Deadline Reminder API

This project provides a REST API for managing tasks and sending reminders. Below are examples of how the API works with Postman.

---

## API Endpoints

### 1. Add Task Endpoint
The `POST /add_task` endpoint allows you to add a task. Below is an example request and response in Postman:

![Add Task API Request Screenshot](images/Screenshot%202024-12-28%20194638.png)

---

### 2. Send Reminders Endpoint
The `GET /send_reminders` endpoint sends reminders for tasks. Below is an example request and response in Postman:

![Postman API Request Screenshot](images/Screenshot%202024-12-28%20165942.png)

---

## Technologies Used
- Python
- Flask
- SQLite
- Flask-Mail

## License

This project is licensed under the MIT License.
---

### Let me know if you need help with any of these steps, like configuring GitHub, writing the README, or taking screenshots!