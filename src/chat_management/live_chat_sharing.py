```python
import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/share_chat', methods=['POST'])
def share_chat():
    data = request.get_json()
    chat_id = data.get('chat_id')
    user_id = data.get('user_id')

    if not chat_id or not user_id:
        return jsonify({'message': 'Missing parameters'}), 400

    chat_data = get_chat_data(chat_id)
    if not chat_data:
        return jsonify({'message': 'Chat not found'}), 404

    share_link = generate_share_link(chat_id, user_id)
    return jsonify({'share_link': share_link}), 200

def get_chat_data(chat_id):
    # This function should interact with your database and return the chat data
    # For the purpose of this example, we'll return a dummy chat data
    return {'chat_id': chat_id, 'messages': []}

def generate_share_link(chat_id, user_id):
    # This function should generate a unique share link for the chat
    # For the purpose of this example, we'll return a dummy share link
    return f'http://localhost:5000/view_chat/{chat_id}?user_id={user_id}'

@socketio.on('new-message')
def handle_new_message(data):
    chat_id = data.get('chat_id')
    message = data.get('message')
    user_id = data.get('user_id')

    # Here you should add the message to the chat in your database
    # And then emit the new message to all clients

    emit('new-message', {'chat_id': chat_id, 'message': message, 'user_id': user_id}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```