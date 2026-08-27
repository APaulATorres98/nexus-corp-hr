from flask import Flask, request, jsonify

app = Flask(__name__)

EMPLOYEES_DB = {
    1: {"id": 1, "name": "Ana Pérez", "role": "HR Manager", "salary": 45000, "email": "ana.perez@nexuscorp.com"},
    2: {"id": 2, "name": "Carlos Gómez", "role": "Software Engineer", "salary": 38000, "email": "carlos.gomez@nexuscorp.com"},
    3: {"id": 3, "name": "María López", "role": "Financial Analyst", "salary": 40000, "email": "maria.lopez@nexuscorp.com"}
}

@app.route('/')
def home():
    return jsonify({"message": "Nexus Corp HR Portal API v1.0"})

@app.route('/api/hr/employee/<int:emp_id>', methods=['GET'])
def get_employee_profile(emp_id):
    employee = EMPLOYEES_DB.get(emp_id)
    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({"error": "Empleado no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
