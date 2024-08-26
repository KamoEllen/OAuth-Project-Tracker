
# A Simple CRUD API with OAuth using FastAPI

This repository contains a simple CRUD API built with FastAPI and OAuth authentication. It provides endpoints for managing projects, including creating, reading, updating, and deleting projects. 

**Note:** Currently, Railway is used for testing instead of MongoDB. Integration with MongoDB is planned for future updates.

## Installation

To get started, you'll need to install the required packages. Run the following command:

```bash
pip install -r requirements.txt
```

## Project Structure

<details>
<summary>Project Structure Overview</summary>

```plaintext
C:.
├───app                 # Main application code
│   └───__app.py__      # Compiled Python files
│   └───__db.py__       
│
├───auth                # Authentication functionality
│   └───__init__.py__   # Compiled Python files
│   └───__auth_bearer.py__  
│   └───__auth_handler.py__  
│
├───models              # Folder containing data models
│   └───__models.py__   # Compiled Python files 
│
├───routes              # Folder containing app routes
│   └───__project_routes.py__  
│   └───__user_routes.py__  
│   
├───main.py            # Main entry point for the application
├───.env               # Environment variables file
│   └───DATABASE_URL=your_database_url
│   └───SECRET_KEY=your_secret_key
└───Procfile            # Deployment config file
    └───web: uvicorn app.app:app 
```
</details>

## API Endpoints

<details>
<summary>API Endpoints Overview</summary>

### Create Project

- **Endpoint:** `POST /project/`
- **Description:** Creates a new project and returns the created project including its unique identifier.

### Get Project List

- **Endpoint:** `GET /project/`
- **Description:** Retrieves a list of all projects, each including its unique identifier and date fields.

### Get Project By ID

- **Endpoint:** `GET /project/{id}`
- **Description:** Retrieves a single project by its unique identifier.

### Update Project

- **Endpoint:** `PUT /project/{id}`
- **Description:** Updates an existing project, including its date fields.

### Delete Project

- **Endpoint:** `DELETE /project/{id}`
- **Description:** Deletes a project by its unique identifier.

</details>

## Project Enhancements and Changes

<details>
<summary>Project Enhancements and Changes</summary>

### Added Unique Identifiers

- **ObjectId for Projects:** Introduced a unique identifier for each project using MongoDB's `ObjectId`. This ensures that each project has a distinct identifier.

  - **Implementation Details:** 
    - Modified the `project_parser` function in `db.py` to include `id` derived from `_id` of the project document.
    - Updated the `add_project` function to return the project with its unique identifier.

### Added Date Fields

- **Date Fields:** Added `startDate` and `endDate` fields to the `ProjectSchema` for better project management.

  - **Implementation Details:**
    - Updated the `ProjectSchema` model in `models.py` to include `startDate` and `endDate` as `datetime` fields.
    - Modified the `project_parser` function in `db.py` to return `startDate` and `endDate` fields.
    - Updated the `ProjectSchema` and `UpdateProjectModel` to handle date inputs correctly.

### Updated API Endpoints

- **Create Project Endpoint:** The `POST /project/` endpoint now returns the newly created project including its unique identifier.

- **Get Project List Endpoint:** The `GET /project/` endpoint returns a list of projects, each including its unique identifier and date fields.

- **Get Project By ID Endpoint:** The `GET /project/{id}` endpoint allows retrieval of a single project by its unique identifier.

- **Update Project Endpoint:** The `PUT /project/{id}` endpoint now supports updating project details, including the date fields.

- **Delete Project Endpoint:** The `DELETE /project/{id}` endpoint allows deletion of a project by its unique identifier.

### Other Notable Changes

- **Error Handling:** Improved error responses in `project_routes.py` to handle scenarios where a project does not exist or updates fail.

- **Response Models:** Used `ResponseModel` and `ErrorResponseModel` for standardized API responses.

- **Date Format Handling:** Updated date format handling in `ProjectSchema` and `UpdateProjectModel` to use `datetime` for consistent date-time representation.



### Future Improvements

- **Enhanced Validation:** Plan to enhance validation and add more robust error handling.
- **Performance Optimization:** Consider adding pagination and caching mechanisms for performance improvements.
- **Security Enhancements:** Review and implement additional security measures and authentication improvements.

</details>

### Screenshot
![Description of Image](https://github.com/KamoEllen/OAuth-Project-Tracker/blob/main/img.png?raw=true)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or fixes.


## Contact

For any questions or comments, please reach out to [kamoellenkganakga@gmail.com](mailto:kamoellenkganakga@gmail.com).

---

Thank you for checking out my FastAPI CRUD API project! 🚀

