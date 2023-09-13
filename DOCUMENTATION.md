# Person REST API Documentation


<!-- Back to Top Navigation Anchor -->
<a name="documentation-top"></a>

Welcome to the documentation for the Person REST API project. This documentation provides all the necessary information to set up, use, and understand the API.


---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Introduction"> Introduction </a>
    </li>
    <li><a href="#Getting-Started">Getting Started</a></li>
    <li><a href="#API-Endpoints">API Endpoints/a></li>
    <li><a href="#Request/Response-Formats">Request/Response Formats</a></li>
    <li><a href="#Sample-API-Usage">Sample API Usage</a></li>
    li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
  <p align="right"><a href="#documentation-top">back to top</a></p>
</details>


## Introduction

The Person REST API allows you to perform CRUD (Create, Read, Update, Delete) operations on individual records. You can create, retrieve, update, and delete person records while ensuring data integrity and input validation.


## Getting Started


### Prerequisites
Before using the API, ensure you have the following prerequisites installed:

Python (3.11 recommended)
Django
Django REST framework
PostgreSQL (or your preferred database)
Gunicorn (for deployment)

### Installation
1. Clone the GitHub repository:

git clone https://github.com/your-username/person-api-project.git

2. Navigate to the project directory:

cd person-api-project

3. pip install -r requirements.txt

pip install -r requirements.txt

4. Create and configure your database in settings.py.

5. Apply migrations:

python manage.py migrate

6. Start the development server:

python manage.py runserver


The API should now be accessible at http://localhost:8000/api

## API Endpoints

GET /api
Retrieve a list of all persons.

Parameters:
None.

Response:

Status Code: 200 (OK)

Response Format: JSON

Example Response Body:

```
[
  {
    "id": 1,
    "name": "Mark Essien"
  },
  {
    "id": 2,
    "name": "James Smith"
  }
]
```


GET /api/{id}
Retrieve details of a person by their ID.

Parameters:

id (integer): The unique ID of the person.
Response:

Status Code: 200 (OK)

Response Format: JSON

Example Response Body:
```
{
  "id": 1,
  "name": "Mark Essien"
}
```

GET /api/?name={name}
Retrieve details of a person by their name.

Parameters:

name (string): The name of the person.
Response:

Status Code: 200 (OK)

Response Format: JSON

Example Response Body:
```
{
  "id": 1,
  "name": "Mark Essien"
}
```

POST /api
Create a new person record.

Request:

Request Format: JSON

Example Request Body:
```
{
  "name": "Alice Johnson"
}
```
Response:

Status Code: 201 (Created)

Response Format: JSON

Example Response Body:

```
{
  "id": 3,
  "name": "Alice Johnson"
}
```

PUT /api/{id}
Update details of an existing person by their ID.

Parameters:

id (integer): The unique ID of the person to update.
Request:

Request Format: JSON

Example Request Body:
```
{
  "name": "Updated Name"
}
```
Response:

Status Code: 200 (OK)

Response Format: JSON

Example Response Body:

```
{
  "id": 1,
  "name": "Updated Name"
}
```

DELETE /api/{id}
Delete a person by their ID.

Parameters:

id (integer): The unique ID of the person to delete.
Response:

Status Code: 204 (No Content)


## Request/Response Formats
Person Object
The person object in request and response bodies has the following format:

id (integer): The unique ID of the person.
name (string): The name of the person.
Example:
```
{
  "id": 1,
  "name": "John Doe"
}
```


## Sample API Usage
Here are some sample use cases for the Person REST API:

- Creating a new person:

POST /api/persons/
```
{
  "name": "Eve Johnson"
}
```

- Updating an existing person:
PUT /api/persons/1/
```
{
  "name": "Updated Name"
}
```
- Retrieving a person by ID:
```
GET /api/persons/1/
```

- Retrieving a person by name:
```
GET /api/persons/?name=John Doe
```

- Deleting a person:
```
DELETE /api/persons/1/
```


## Deployment
For deployment instructions using Gunicorn and other relevant details, please refer to the Deployment section in the project's GitHub repository.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have ideas for improvements, please create an issue or submit a pull request on GitHub.











---