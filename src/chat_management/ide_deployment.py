```python
import os
import subprocess

def deploy_to_ide(user_id, chat_id):
    """
    Function to deploy the chat to an IDE for further development.
    """
    # Define the path to the chat file
    chat_file_path = f"chats/{user_id}/{chat_id}.py"

    # Check if the chat file exists
    if not os.path.exists(chat_file_path):
        raise Exception("Chat file does not exist.")

    # Define the command to open the chat file in the IDE
    # Here we use Visual Studio Code as an example, replace 'code' with the command to open your preferred IDE
    command = f"code {chat_file_path}"

    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output and error from the command
    stdout, stderr = process.communicate()

    # If there is an error, raise an exception
    if process.returncode != 0:
        raise Exception(f"Failed to open chat in IDE. Error: {stderr.decode()}")

    return f"Chat {chat_id} successfully opened in IDE."
```