from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import face_recognition
import base64
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)

# Connect to MongoDB database
#MONGO_URI = 
#client = MongoClient(MONGO_URI)
#db = 

# Helper Functions
def save_profile_picture(image_data):
    image_data = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    face_locations = face_recognition.face_locations(img)
    if face_locations:
        # Save image to file system or cloud storage
        file_path = f"./images/{str(ObjectId())}.jpg"
        cv2.imwrite(file_path, img)
        return file_path
    else:
        return None

@app.route('/api/signup/patient', methods=['POST'])
def signup_patient():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    patient = {
        "name": data['name'],
        "email": data['email'],
        "password": hashed_password,
        "gender": data['gender'],
        "age": data['age'],
        "contact_preference": data['contact_preference'],
        "weight": data['weight'],
        "height": data['height'],
        "mental_state": data['mental_state'],
        "medications": data['medications'],
        "profile_picture": save_profile_picture(data['profile_picture']),
        "diagnosis": data.get('diagnosis', '')  # Adding diagnosis field
    }
    db.patients.insert_one(patient)
    return jsonify({"message": "Patient signed up successfully"}), 201

@app.route('/api/signup/doctor', methods=['POST'])
def signup_doctor():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    doctor = {
        "name": data['name'],
        "email": data['email'],
        "password": hashed_password,
        "age": data['age'],
        "specialization": data['specialization'],
        "experiences": data['experiences'],
        "bio": data['bio'],
        "gender": data['gender']
    }
    db.doctors.insert_one(doctor)
    return jsonify({"message": "Doctor signed up successfully"}), 201

# Remaining routes and logic
@app.route("/api/test")
def test():
    data = list(db.doctors)
    return jsonify(data)

@app.route("/api/patients")
def get_patients():
    patients = list(db["patients"].find())
    patients = get_patient_status(patients)
    return jsonify(patients)

@app.route('/api/recognize', methods=['POST'])
def recognize():
    data = request.get_json()
    image_data = data['image']
    img = save_profile_picture(image_data)
    return jsonify({"message": "Image processed", "img_path": img})

def get_patient_status(patients):
    # Assuming vitals_model is defined elsewhere
    X = [[p["pulse"], convert_bp(p["blood_pressure"]), p["temperature"]] for p in patients]
    X = StandardScaler().fit_transform(X)
    y = vitals_model.predict(X)
    status_mapping = {0: "Normal", 1: "Critical", 2: "Emergency"}
    for i, p in enumerate(patients):
        p["_id"] = str(p["_id"])  # Convert ObjectId to string
        p["status"] = status_mapping.get(int(y[i][0]), "Unknown")
    return patients

def convert_bp(bp):
    numerator, denominator = bp.split("/")
    numerator = float(numerator)
    denominator = float(denominator)
    return (numerator + denominator) / 2

if __name__ == '__main__':
    app.run(debug=True)
