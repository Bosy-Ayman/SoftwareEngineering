# Learners API

This API allows you to manage learners by performing basic CRUD operations (Create, Read, Update, and Delete). The API is built using Flask and provides endpoints to get all learners, create a new learner, update an existing learner, delete a learner, and retrieve a learner by their ID.

## Installation

1. Clone the repository.
2. Install the required Python packages using pip:

   ```bash
   pip install Flask
Run the Flask app:


python app.py
The API will run locally on http://localhost:5000/.

Endpoints
1. Get All Learners
URL: /learners/
Method: GET
Response:
200 OK with a list of all learners.
2. Create a Learner
URL: /learners/
Method: POST
Request Body:
JSON:
json
{

  "ID": "1",
  "name": "Bosy",
  "major": "CSAI"
}
Response:
201 Created with the updated list of learners.
3. Update Learner by ID
URL: /learners/<id>
Method: PUT
Request Body:
JSON:
json

Response:

200 OK with the updated learner details.
404 Not Found if the learner ID doesn't exist.
4. Delete Learner by ID
URL: /learners/<id>
Method: DELETE

Response:
204 No Content if the learner is deleted successfully.
404 Not Found if the learner ID doesn't exist.
5. Get Learner by ID
URL: /learners/<id>
Method: GET

Response:
200 OK with the learner's details.
404 Not Found if the learner ID doesn't exist.
Example Requests
Create a Learner

bash

Get All Learners
bash
curl http://localhost:5000/learners/
