
## Overview

The **AST Rule Engine** is a 3-tier application designed to dynamically evaluate rules using Abstract Syntax Trees (ASTs). This project showcases the implementation of a scalable rule evaluation system, enabling users to manage business rules effectively through a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Conclusion](#conclusion)


## Features

- **Dynamic Rule Evaluation**: The engine evaluates rules at runtime, providing flexibility and adaptability to business needs.
- **3-Tier Architecture**: The design separates the User Interface, API, and Backend for improved maintainability and scalability.
- **CRUD Functionality**: Users can Create, Read, Update, and Delete rules easily via the application.
- **Scalability**: The architecture is designed to efficiently manage an increasing number of rules and requests.
- **User-Friendly Interface**: The application features a straightforward and intuitive UI for better user experience.

## Technologies

The following technologies and frameworks were utilized in the development of the AST Rule Engine:

- **Frontend**: HTML, CSS, JavaScript (or specific frameworks, e.g., React)
- **Backend**: Flask (Python)
- **Database**: SQLite
- **AST Library**: Python's built-in `ast` module

## Installation

To set up the AST Rule Engine on your local machine, follow these instructions:

1. **Clone the Repository**:
   
   git clone https://github.com/stasleem693/AST-rule-engine.git
   cd ast-rule-engine

   ## Usage

Once the application is running:

1. **Navigate to the User Interface**: Open your web browser and go to `http://localhost:5000` to access the user interface of the Rule Engine.

2. **Manage Rules**: Use the interface to create, read, update, and delete rules as per your business requirements. You can input the rule conditions and actions through the form provided in the UI.

3. **Evaluate Rules**: After adding rules, you can evaluate them based on specific input data directly from the UI.

4. **Access the API**: For programmatic interactions, utilize the API endpoints available at `http://localhost:5000/api/rules`. You can send requests to create or manage rules programmatically.

5. **Example API Request**: To create a new rule, you can send a POST request to `/api/rules` with the following JSON payload:
    ```json
    {
      "name": "Example Rule",
      "condition": "x > 10",
      "action": "Alert"
    }
    ```
   This allows you to integrate the Rule Engine with other applications or services as needed.

## API Documentation

### Endpoints

- **GET /api/rules**
  - **Description**: Retrieve all existing rules.
  - **Response**: Returns a JSON array of rule objects.

- **POST /api/rules**
  - **Description**: Create a new rule.
  - **Request Body**:
    ```json
    {
      "name": "Example Rule",
      "condition": "x > 10",
      "action": "Alert"
    }
    ```
  - **Response**: Returns the created rule object.

- **GET /api/rules/{id}**
  - **Description**: Retrieve a specific rule by ID.
  - **Response**: Returns a JSON object of the requested rule.

- **PUT /api/rules/{id}**
  - **Description**: Update a specific rule by ID.
  - **Request Body**:
    ```json
    {
      "name": "Updated Rule",
      "condition": "x < 5",
      "action": "Notify"
    }
    ```
  - **Response**: Returns the updated rule object.

- **DELETE /api/rules/{id}**
  - **Description**: Delete a specific rule by ID.
  - **Response**: Returns a success message or confirmation.

- **POST /api/evaluate**
  - **Description**: Evaluate rules based on provided input data.
  - **Request Body**:
    ```json
    {
      "data": {
        "x": 15
      }
    }
    ```
  - **Response**: Returns evaluation results based on the applied rules.
 
  - ## Conclusion

Thank you for exploring the **AST Rule Engine** project! This application showcases the power of dynamic rule evaluation using Abstract Syntax Trees. We believe that this system can greatly enhance business decision-making processes by providing a flexible and user-friendly interface for managing rules. 

We welcome feedback and contributions from the community to make this project even better. If you have any questions or suggestions, please feel free to reach out. Happy coding!
