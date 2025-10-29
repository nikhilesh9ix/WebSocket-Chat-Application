#!/usr/bin/env python3
"""
Flask WebSocket Chat Application Backend
Real-time chat server using Flask-SocketIO for WebSocket communication
"""

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

# Store connected users
connected_users = {}
message_history = []

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Handle new client connection"""
    client_id = request.sid
    user_name = f"User_{client_id[:8]}"
    
    # Store user info
    connected_users[client_id] = {
        'name': user_name,
        'joined_at': datetime.now()
    }
    
    print(f"🟢 {user_name} connected (ID: {client_id})")
    print(f"👥 Total users online: {len(connected_users)}")
    
    # Send welcome message to the user
    emit('user_joined', {
        'message': f"Welcome to the chat, {user_name}!",
        'user_name': 'System',
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'type': 'system'
    })
    
    # Broadcast to all other users
    emit('user_joined', {
        'message': f"{user_name} has joined the chat",
        'user_name': 'System',
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'type': 'join'
    }, broadcast=True, include_self=False)
    
    # Send recent message history to new user
    for msg in message_history[-10:]:  # Last 10 messages
        emit('receive_message', msg)
    
    # Update user count
    emit('user_count', {'count': len(connected_users)}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    client_id = request.sid
    
    if client_id in connected_users:
        user_name = connected_users[client_id]['name']
        del connected_users[client_id]
        
        print(f"🔴 {user_name} disconnected (ID: {client_id})")
        print(f"👥 Total users online: {len(connected_users)}")
        
        # Broadcast to all remaining users
        emit('user_left', {
            'message': f"{user_name} has left the chat",
            'user_name': 'System',
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': 'leave'
        }, broadcast=True)
        
        # Update user count
        emit('user_count', {'count': len(connected_users)}, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    """Handle incoming chat messages"""
    client_id = request.sid
    
    if client_id not in connected_users:
        return
    
    user_name = connected_users[client_id]['name']
    message = data.get('message', '').strip()
    
    if not message:
        return
    
    # Create message object
    message_data = {
        'message': message,
        'user_name': user_name,
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'type': 'message',
        'user_id': client_id[:8]
    }
    
    # Store in history
    message_history.append(message_data)
    
    # Keep only last 100 messages
    if len(message_history) > 100:
        message_history.pop(0)
    
    print(f"💬 {user_name}: {message}")
    
    # Broadcast to all users
    emit('receive_message', message_data, broadcast=True)

@socketio.on('set_username')
def handle_set_username(data):
    """Handle username change"""
    client_id = request.sid
    new_name = data.get('username', '').strip()
    
    if not new_name or client_id not in connected_users:
        return
    
    old_name = connected_users[client_id]['name']
    connected_users[client_id]['name'] = new_name
    
    print(f"📝 {old_name} changed name to {new_name}")
    
    # Broadcast name change
    emit('user_renamed', {
        'message': f"{old_name} is now known as {new_name}",
        'user_name': 'System',
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'type': 'rename'
    }, broadcast=True)

@socketio.on('typing')
def handle_typing(data):
    """Handle typing indicators"""
    client_id = request.sid
    
    if client_id not in connected_users:
        return
    
    user_name = connected_users[client_id]['name']
    is_typing = data.get('typing', False)
    
    # Broadcast typing status to others
    emit('user_typing', {
        'user_name': user_name,
        'typing': is_typing
    }, broadcast=True, include_self=False)

if __name__ == '__main__':
    print("🚀 Starting Flask WebSocket Chat Server...")
    print("=" * 50)
    print("🌐 Server will run on http://localhost:5000")
    print("💡 Open multiple browser tabs to test multi-user chat")
    print("=" * 50)
    
    # Run the server
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)