from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    leave_reason = db.Column(db.Text, nullable=False)
    leave_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default='pending')