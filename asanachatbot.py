import json
import requests

# Set up the Asana API endpoint and header
endpoint = "https://app.asana.com/api/1.0/tasks"
header = {"Authorization": "Bearer YOUR_ASANA_ACCESS_TOKEN"}

# Define the function that retrieves the last Asana update
def get_last_asana_update():
    # Send a GET request to the Asana API endpoint
    response = requests.get(endpoint, headers=header)

    # Parse the response JSON
    tasks = json.loads(response.text)["data"]

    # Find the most recently modified task
    last_modified_task = max(tasks, key=lambda x: x["modified_at"])

    # Extract the task name and modification time
    task_name = last_modified_task["name"]
    modified_time = last_modified_task["modified_at"]

    # Format the modification time as a string
    modified_time_str = modified_time[:10] + " at " + modified_time[11:16]

    # Return a string with the task name and modification time
    return f"The last Asana update was on {modified_time_str}. The latest task is {task_name}."

# Define the chatbot function
def chatbot(message):
    # Check if the message is a request for feedback
    if "feedback" in message.lower():
        # Get the last Asana update and return it as a response
        response = get_last_asana_update()
        return response

    # If the message is not a request for feedback, return a generic response
    return "I'm sorry, I don't understand. Could you please clarify?"

# Test the chatbot function
if __name__ == '__main__':
    print(chatbot("Can you give me some feedback on the project?"))