# **Inventory App (Flask + MongoDB)**

**Repository**: [Inventory-flask-mongodb](https://github.com/yoftil7/Inventory-flask-mongodb)  
**Version**: 1.0  
**Developer**: Yoftahie Alem

## **Overview**
This is a Flask-based inventory management system designed to track and manage inventory items using a MongoDB database for persistent storage. The application allows users to create, read, update, and delete (CRUD) inventory items in a flexible and scalable way.

## **Key Features**
- CRUD operations for inventory items (Create, Read, Update, Delete)
- Data stored in a MongoDB database
- Flask-based backend logic
- Simple RESTful API structure
- Modular codebase with utility functions and tests

## **Tech Stack**
- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Package Management**: `pip` (via `requirements.txt`)
- **Testing**: Unit tests provided in the `tests` directory
- **Packaging**: Set up for easy distribution with `setup.py`

## **Project Structure**

- **`build/`**: Contains build-related files.
- **`dist/`**: Distribution-ready build files.
- **`instance/`**: Flask instance-related configuration and files.
- **`inventory/`**: Core application logic, routes, and models.
- **`tests/`**: Contains unit tests to ensure the functionality of the app.
- **`.DS_Store`**: macOS system file (ignore this).
- **`MANIFEST.in`**: Lists additional files to be included in the source distribution.
- **`README.md`**: The project’s readme file (you are reading this).
- **`build.sh`**: Script to build the project.
- **`run.sh`**: Script to run the project locally.
- **`setup.cfg`**: Configuration file for the packaging process.
- **`setup.py`**: The script for installing the app as a Python package.
- **`requirements.txt`**: Lists the Python dependencies required to run the app.

## **System Requirements**
- Python 3.x
- MongoDB

## **Installation and Setup**

### **Clone the Repository**
```bash
git clone https://github.com/yoftil7/Inventory-flask-mongodb.git
cd Inventory-flask-mongodb
```

### **Install Dependencies**
Make sure you have Python 3 and `pip` installed. Install the required dependencies with:

```bash
pip install -r requirements.txt
```

### **Set up MongoDB**
Ensure you have a MongoDB instance running locally or via a cloud provider like MongoDB Atlas.

### **Run the Application**
To start the application, run the `build.sh` and `run.sh` scripts:

```bash
sh build.sh
sh run.sh
```

Alternatively, you can manually run the app:

```bash
python3 inventory/main.py
```

The app will start on `http://localhost:5000` by default. You can change this in the Flask configuration if needed.

## **Usage**
- Access the inventory management app via `http://localhost:5000`.
- Use the REST API to perform the following:
  - **Create**: Add new inventory items.
  - **Read**: View existing inventory.
  - **Update**: Modify existing inventory items.
  - **Delete**: Remove items from the inventory.

## **Testing**
Unit tests are provided in the `tests/` directory. You can run the tests using:

```bash
python -m unittest discover -s tests
```

This will ensure that all components of the app are working correctly.

## **Future Enhancements**
- Migrate to a containerized setup using Docker (already implemented in the latest version).
- Implement user authentication and role-based access control.
- Create a user-friendly front-end interface.
- Add search and filtering functionality to the API.

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
