# 🔄 COMP2001 Trail Management System

## 📄 Project Description
The **Trail Management System** is a web-based API developed to facilitate the management of trails. It enables users to create, read, update, and delete trail records stored in a SQL database. The system uses Flask as the backend framework and integrates seamlessly with an Azure-hosted SQL database.

---

## 🔧 Features

- **Authentication**
  - Role-based access control (e.g., Admin privileges for creating, updating, and deleting trails).
- **CRUD Operations**
  - Create, Read, Update, and Delete trail records.
- **Database Integration**
  - Microsoft SQL Server hosted on Azure.
- **API Documentation**
  - Includes interactive Swagger API documentation.

---

## 🎨 Technologies Used

- **Backend**: Flask, Flask-RESTful, Swagger
- **Database**: Microsoft SQL Server (Azure-hosted)
- **Tools**: Postman for API testing, Visual Studio Code for development

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

## 💡 Usage Instructions

### 1. Start the Flask Application
```bash
python app.py
```
The application will run on [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 2. Test the API in Postman
#### Example Request for Creating a Trail
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

## 🔧 Troubleshooting

### Common Issues
1. **Database Connection Errors**:
   - Ensure your Azure SQL database credentials are correct.
   - Verify that your IP is whitelisted in the Azure SQL Server firewall settings.
2. **500 Internal Server Errors**:
   - Check the Flask logs for debugging information.
   - Validate your API requests using Postman.

---

## 🌍 Future Enhancements
- Implement token-based authentication using JWT.
- Add support for frontend frameworks like React.
- Enable trail image uploads.

---

## 🙏 Acknowledgements
Special thanks to the University of Plymouth and the COMP2001 module staff for their guidance and support throughout this project.
