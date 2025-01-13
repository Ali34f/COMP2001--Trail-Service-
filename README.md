# 🔄 COMP2001 Trail Management System

## 📄 Project Description
The **Trail Management System** is a web-based API developed to facilitate the management of trails. It enables users to create, read, update, and delete trail records stored in a SQL database. The system uses Flask as the backend framework and integrates seamlessly with an Azure-hosted SQL database.

---

## 🔧 Features

- **Authentication & Authorization**
  - Role-based access control using JWT (e.g., Admin privileges for creating, updating, and deleting trails).
- **Trail Mananagement**
  - Full CRUD operations for trail records.
- **Database Integration**
  - Powered by Microsoft SQL Server hosted on Azure.
- **Interactive API Documentation**
  - Swagger UI integration for easy API testing and exploration.
- **Front-end Integration**
  - Simple fornt-end interface using HTML, CSS, and JavaScript for managing trails.

---

## 💻 Technologies Used

- **Backend**: Python,Flask, Flask-RESTful
- **Database**: Microsoft SQL Server (Azure-hosted)
- **Documenation**: Swagger (Flasgger)
- **Frontend**: HTML, CSS, JavaScript
- **Tools**: Postman for API testing, Visual Studio Code 
- **Deployment**: Docker

---

## 🔎 Prerequisites

1. Python 3.9+
2. Required Python Libraries:
   - Flask
   - Flask-RESTful
   - pyodbc
   - flasgger
3. Microsoft SQL Server
4. Visual Studio Code
5. Postman (for testing)
6. Docker (for containerized deployment)

---

## 🚀 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ali34f/COMP2001--Trail-Service-
cd trail-management-system
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Connection
- Update the `database_connection.py` file with your Azure SQL database connection string.
---
### Running with Docker 

1.  Pull the Docker Image 
```bash
docker pull jahinkhan/comp2001-trail-service:latest
```
2.  Run the Docker Container
```bash
docker run -d -p 5000:5000 jahinkhan/comp2001-trail-service:latest
```
3.  Access the Applicattion open http://127.0.0.1:5000/apidocs  in your browser 


---

## 💡 Usage Instructions

### 1. Start the Flask Application
```bash
python app.py
```
The application will run on [http://127.0.0.1:5000](http://127.0.0.1:5000).
#### Interact with the API
- Open [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs) for Swagger UI.
- User Postman to test API ednpoints or interact with the front end at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 2. Test the API in Postman
#### Create a Trail (Admin Only)
- **Endpoint**: `POST /trails`
- **Request Body**:
```json
{
    "Trail_name": "Mountain Trail",
    "Trail_Summary": "A scenic trail",
    "Trail_Description": "A challenging and rewarding hike.",
    "Difficulty": "Hard",
    "Location": "Mountain Range",
    "Length": 10.5,
    "Elevation_gain": 1200,
    "Route_type": "Loop",
    "OwnerID": 1
}




```


---

## 📈 Project Structure
```plaintext
.
├── app.py                # Main Flask application
├── database_connection.py # Database connection utility
├── crud_operations.py    # CRUD operation functions
├── authenticator.py      # User authentication functions
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── sql/                  # SQL scripts for procedures and testing
│   ├── create.sql
│   ├── read.sql
│   ├── update.sql
│   ├── delete.sql
│   └── testing_procedures.sql
└── templates/
    └── index.html        # Frontend template
```
---

## 🔗 Key Endpoints
| **Method** | **Endpoint**       | **Description**             | **Authentication** |
|------------|--------------------|-----------------------------|--------------------|
| `POST`     | `/auth`            | Authenticate user and get JWT | No                |
| `GET`      | `/trails`          | Retrieve all trails         | Yes               |
| `GET`      | `/trails/{id}`     | Retrieve trail by ID        | Yes               |
| `POST`     | `/trails`          | Create a new trail          | Admin             |
| `PUT`      | `/trails/{id}`     | Update trail by ID          | Admin             |
| `DELETE`   | `/trails/{id}`     | Delete trail by ID          | Admin             |
---

## 🔧 Troubleshooting

### Common Issues
1. **Database Connection Errors**:
   - Ensure your Azure SQL database credentials are correct.
   - Verify that your IP is whitelisted in the Azure SQL Server firewall settings.
2. **500 Internal Server Errors**:
   - Check the Flask logs for debugging information.
   - Validate your API requests using Postman.

---

## 🔮 Future Enhancements
- Integrate advanced analystics for trail popularity and usage.
- Implement chachig for faster trail retrieval
- Mobile App Integration: Extend functionality for mobile devices 

---

## 🙏 Acknowledgements
Special thanks to the University of Plymouth and the COMP2001 module staff for their guidance and support throughout this project.
