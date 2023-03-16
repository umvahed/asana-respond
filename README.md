# asana-respond

In this example, the chatbot function takes a message as input and checks if the message contains the word "feedback". If it does, the function calls the get_last_asana_update function to retrieve the last update on Asana and returns it as a response. If the message is not a request for feedback, the chatbot returns a generic response.

You would need to replace "YOUR_ASANA_ACCESS_TOKEN" with your actual Asana access token to make this code work. Additionally, this code only retrieves the most recently modified task from Asana; if you want to retrieve a more specific task or set of tasks, you would need to modify the code accordingly.