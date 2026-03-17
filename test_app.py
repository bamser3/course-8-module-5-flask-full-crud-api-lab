from app import app
import json

# Create a test client
client = app.test_client()

# GET all events
response = client.get("/events")
print("GET /events:", response.status_code, response.get_json())

# POST a new event
response = client.post(
    "/events",
    data=json.dumps({"title": "Hackathon"}),
    content_type="application/json"
)
print("POST /events:", response.status_code, response.get_json())

# PATCH an existing event
response = client.patch(
    "/events/1",
    data=json.dumps({"title": "Updated Tech Meetup"}),
    content_type="application/json"
)
print("PATCH /events/1:", response.status_code, response.get_json())

# DELETE an event
response = client.delete("/events/2")
print("DELETE /events/2:", response.status_code, response.get_json())