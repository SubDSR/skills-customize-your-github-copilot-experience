# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that can create, read, update, and delete records in memory. You will practice route design, request validation, and automatic API documentation.

## 📝 Tasks

### 🛠️ Create the API App

#### Description
Set up a FastAPI application with a clear resource model, a root route, and a route that returns all records.

#### Requirements
Completed program should:

- Create a FastAPI app in Python.
- Define at least one resource type, such as `books`, `tasks`, or `students`.
- Include a `GET /` route that returns a simple welcome message.
- Include a `GET /<resource>` route that returns the current collection.
- Return JSON responses.

### 🛠️ Implement CRUD Endpoints

#### Description
Add endpoints that let users create a new record, view one record by ID, update an existing record, and delete a record.

#### Requirements
Completed program should:

- Support `POST` to create a new record.
- Support `GET /<resource>/{id}` to retrieve one record.
- Support `PUT` or `PATCH` to update one record.
- Support `DELETE` to remove one record.
- Use an in-memory list or dictionary to store data.
- Return the correct HTTP status codes for success and missing records.

### 🛠️ Validate Input and Document the API

#### Description
Use Pydantic models to validate incoming data and confirm that the API is documented through FastAPI's built-in docs.

#### Requirements
Completed program should:

- Define a Pydantic model for the request body.
- Reject invalid data such as missing required fields or the wrong data type.
- Include at least one field with validation beyond plain text, such as a number, boolean, or constrained string.
- Make sure the API can be explored in the automatic documentation at `/docs`.
- Show an example request and response in your README or inline comments.
