from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, LeaveRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leave_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/leave-requests', methods=['GET'])
def get_leave_requests():
    requests = LeaveRequest.query.all()
    return jsonify([{
        'id': request.id,
        'studentName': request.student_name,
        'leaveReason': request.leave_reason,
        'leaveDate': request.leave_date.isoformat(),
        'returnDate': request.return_date.isoformat(),
        'status': request.status
    } for request in requests])

@app.route('/api/leave-requests', methods=['POST'])
def create_leave_request():
    data = request.json
    new_request = LeaveRequest(
        student_name=data['studentName'],
        leave_reason=data['leaveReason'],
        leave_date=datetime.strptime(data['leaveDate'], '%Y-%m-%d').date(),
        return_date=datetime.strptime(data['returnDate'], '%Y-%m-%d').date()
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"message": "请假申请已提交！"}), 201

@app.route('/api/leave-requests/<int:request_id>', methods=['PUT'])
def update_leave_request(request_id):
    data = request.json
    request = LeaveRequest.query.get(request_id)
    if request:
        request.status = data['status']
        db.session.commit()
        return jsonify({"message": "请假申请已审批！"})
    return jsonify({"message": "未找到请假申请"}), 404

if __name__ == '__main__':
    app.run(debug=True)