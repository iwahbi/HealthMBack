# Healthcare Management System - Backend

A robust backend for the Healthcare Management System built with Flask and MongoDB. This backend provides RESTful APIs for managing patient and doctor profiles, handling health data, and delivering predictive health insights using machine learning models. The system also includes secure profile picture verification with facial recognition.

## Features

- **Patient Management**: APIs for patient sign-up, profile updates, and health data management.
- **Doctor Management**: APIs for doctor sign-up, profile updates, and specialization management.
- **Predictive Health Insights**: Machine learning models to predict patient health status and recommend treatments.
- **Facial Recognition**: Secure profile picture verification using facial recognition technology.
- **Notifications and Communication**: Support for sending notifications and managing patient-doctor communication.

## Technologies Used

- **Flask**: A micro web framework for building APIs.
- **MongoDB**: A NoSQL database for storing patient and doctor data.
- **TensorFlow and scikit-learn**: Machine learning libraries for predictive health insights.
- **OpenCV and face_recognition**: Libraries for facial recognition and image processing.

## Setup and Run Instructions

### Prerequisites

- Python 3.6+
- MongoDB

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/healthcare-backend.git
    cd healthcare-backend
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up MongoDB and update the `MONGO_URI` in `server.py` with your MongoDB connection string.

5. Run the backend server:
    ```sh
    python server.py
    ```

## API Endpoints

- **Patient Endpoints**:
  - `POST /api/signup/patient`: Sign up a new patient.
  - `GET /api/patients`: Retrieve patient data and health status.

- **Doctor Endpoints**:
  - `POST /api/signup/doctor`: Sign up a new doctor.

- **Image Recognition Endpoint**:
  - `POST /api/recognize`: Process and save profile pictures with facial recognition.

## Notes

- Ensure that the backend server is running and accessible for the frontend to communicate with it.
- Update the backend URL in the frontend code if they are hosted on different domains/ports.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.
