# Person API Task

<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>


<div align="center">
  <h1>Person REST API Task</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API#readme"><strong>Explore the Docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/issues">Report Bug</a>
    ·
    <a href="https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Overview"> Overview </a>
    </li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Technology-Stack">Technology Stack/a></li>
    <li><a href="#How-to-run-the-project-on-Local">How to run the project on Local</a></li>
    <li><a href="#API-Endpoints">API Endpoints</a></li>
    li><a href="#Modelling-Diagram">Modelling Diagram</a></li>
    <li><a href="#Contributions">Contributions</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#Connect-With-Me">Connect With Me</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Blog -->
## Overview

The Person REST API Project is a simple API that provides CRUD (Create, Read, Update, Delete) operations for managing information about individuals. This project demonstrates how to develop a REST API using Django and Django REST framework, allowing you to interact with a PostgreSQL database to create, retrieve, update, and delete person records.




<p align="right"><a href="#readme-top">back to top</a></p>

<!-- Features -->
## Features  

- Create: Add new person records with their name.
- Read: Fetch details of a person by their unique ID or name.
- Update: Modify the details of an existing person.
- Delete: Remove a person from the database.
- Dynamic Parameter Handling: Perform operations on persons by specifying their name.
- Input Validation: Ensures that the "name" field only accepts string values.


## Technology Stack

- Django: A high-level Python web framework.
- Django REST framework: A powerful and flexible toolkit for building RESTful Web APIs.
- PostgreSQL: A popular open-source relational database.
- Gunicorn: A production-ready WSGI HTTP server.
- Render: A cloud platform for hosting web applications.

## How to run the project on Local and on Live Server

1. Clone the repository:
```
https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API.git
```
2. Create and activate a virtual environment (optional but recommended):
 ```
  python3 -m venv venv
  ```

```
source venv/bin/activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```
4. Set up the database:

- Create a PostgreSQL database.
- Update the database configuration in the setting.py file(Person_api).

5. Start the development server using 
```
python manage.py runserver
```
6. Access the API in your web browser or using tools like Postman:
- On local
```
http://127.0.0.1:8000/api
```
- On live Server
```
https://hngperson.onrender.com/api/
```
---

## API Endpoints

- GET /api: Retrieve a list of all persons.
- GET /api/{id}: Retrieve details of a person by their ID.
- GET /api/?name={name}: Retrieve details of a person by their name.
- POST /api: Create a new person record.
- PUT /api/{id}: Update details of an existing person by their ID.
- DELETE /api/{id}: Delete a person by their ID.

---

## Modelling Diagram

Person is primary model with two attributes: id (primary key) and name (str).


+--------------------------+
|       Person             |
+--------------------------+
| - id: int (PK)           |
| - name: str              |
+--------------------------+
|                          |
+--------------------------+


The Person class performs CRUD methods: create(POST), read(GET), update(PUT) and delete(DELETE). 
These methods represent the basic CRUD operations one can perform on a Person resource.

+-------------------------+
|                         |
| + create(POST)          |
| + read(GET)             |
| + update(PUT)           |
| + delete(DELETE)        |
|                         |
+-------------------------+


## Contributions

Contributions to the project are welcome, and users are encouraged to report any issues or provide suggestions for improvement. The project is open-source and licensed under the MIT License, allowing for further development and customization.
---

<p align="right"><a href="#readme-top">back to top</a></p>

---

---

<!-- Contact -->
## Connect With Me

OLUBUNMI OLUWATOBI JAMES - [@ItzOfficialOJ](https://twitter.com/ItzOfficialOJ)


<p align="right"><a href="#readme-top">back to top</a></p>


---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/BrodaOJ56/HNG_INTERNSHIP_CRUD_API.svg?style=for-the-badge
[contributors-url]: https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BrodaOJ56/HNG_INTERNSHIP_CRUD_API.svg?style=for-the-badge
[forks-url]: https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/network/members
[stars-shield]: https://img.shields.io/github/stars/BrodaOJ56/HNG_INTERNSHIP_CRUD_API.svg?style=for-the-badge
[stars-url]: https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/stargazers
[issues-shield]: https://img.shields.io/github/issues/BrodaOJ56/HNG_INTERNSHIP_CRUD_API.svg?style=for-the-badge
[issues-url]: https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/issues
[license-shield]: https://img.shields.io/github/license/BrodaOJ56/HNG_INTERNSHIP_CRUD_API.svg?style=for-the-badge
[license-url]: https://github.com/BrodaOJ56/HNG_INTERNSHIP_CRUD_API/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@ItzOfficialOJ-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/ItzOfficialOJ
[twitter-url]: https://twitter.com/ItzOfficialOJ
