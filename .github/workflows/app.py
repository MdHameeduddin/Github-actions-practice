from flask import Flask, jsonify
app = Flask(__name__)

employees = [
    {"id": 1, "name": "Hameed", "role": "DevOps Intern"},
    {"id": 2, "name": "Yahya", "role": "Python Developer"},
    {"id": 3, "name": "Tameem", "role": "Software Engineer"}
]
name = "Md"
x = 5
y = 10



@app.route("/")
def home():
    return "Employee Management Application is Running!"


@app.route("/employees")
def get_employees():
    return jsonify(employees)


@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee)

    return jsonify({"error": "Employee not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
