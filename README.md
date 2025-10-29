# 🌐 WebSocket Chat Application

A real-time web-based chat application built with **Flask-SocketIO** and **WebSockets** that demonstrates modern client-server communication protocols and real-time data transfer.

## 🏗️ Architecture Overview

This project showcases key **Computer Networks** concepts:

- **Transport Layer (TCP)**: WebSocket protocol built on top of TCP for reliable, bidirectional communication
- **Application Layer**: HTTP for initial handshake, WebSocket for real-time messaging
- **Client-Server Architecture**: Flask backend serves multiple web clients
- **Event-Driven I/O**: Asynchronous message handling with Socket.IO

## 📁 Project Structure

```
📦 WebSocket Chat App
├── 📄 app.py                 # Flask-SocketIO backend server
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # This documentation
├── 📁 templates/
│   └── 📄 index.html         # Frontend chat interface
├── 📄 server.py             # Basic TCP chat server (legacy)
└── 📄 client.py             # Basic TCP chat client (legacy)
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Flask Server

```bash
python app.py
```

You should see:
```
🚀 Starting Flask WebSocket Chat Server...
==================================================
🌐 Server will run on http://localhost:5000
💡 Open multiple browser tabs to test multi-user chat
==================================================
```

### 3. Open Chat in Browser

Navigate to: **http://localhost:5000**

### 4. Test Multi-User Chat

- Open multiple browser tabs/windows
- Set different usernames
- Start chatting in real-time!

## ✨ Features

### 🔥 Core Features
✅ **Real-time Messaging** - Instant message delivery using WebSockets  
✅ **Multi-user Support** - Multiple clients can connect simultaneously  
✅ **User Management** - Dynamic usernames and connection tracking  
✅ **Message History** - Recent messages shown to new users  
✅ **Typing Indicators** - See when others are typing  
✅ **Connection Status** - Live connection/disconnection notifications  

### 🎨 UI/UX Features
✅ **Modern Interface** - Responsive design with gradient backgrounds  
✅ **Message Types** - Different styles for own/other/system messages  
✅ **Timestamps** - All messages include time information  
✅ **User Counter** - Shows number of online users  
✅ **Auto-scroll** - Chat window automatically scrolls to latest messages  
✅ **Mobile Responsive** - Works on desktop and mobile devices  

### � Technical Features
✅ **Event-driven Architecture** - Socket.IO event handling  
✅ **Error Handling** - Graceful handling of disconnections  
✅ **Message Validation** - Input sanitization and length limits  
✅ **Cross-origin Support** - CORS enabled for development  

## 💻 Usage Examples

### Example Chat Session

**Browser Tab 1:**
```
💬 WebSocket Chat
🟢 Connected | 👥 2 users

System: Welcome to the chat, User_12345678!
System: Alice has joined the chat
You: Hello everyone!
Alice: Hi there! How's everyone doing?
You: Great! This WebSocket chat is working perfectly.
```

**Browser Tab 2:**
```
💬 WebSocket Chat  
🟢 Connected | 👥 2 users

System: Welcome to the chat, Alice!
User_12345678: Hello everyone!
You: Hi there! How's everyone doing?
User_12345678: Great! This WebSocket chat is working perfectly.
Alice is typing...
```

### Setting Username
1. Enter desired username in the top input field
2. Click "Set Name" button
3. Username updates for all users in real-time

## 🌐 Network Protocol Details

### WebSocket Communication Flow

1. **HTTP Handshake**: Client requests WebSocket upgrade
2. **Protocol Switch**: Server upgrades to WebSocket protocol
3. **Bidirectional Communication**: Real-time message exchange
4. **Event-based Messaging**: Custom events for different message types

### Socket.IO Events

| Event | Direction | Purpose |
|-------|-----------|---------|
| `connect` | Client → Server | Initial connection |
| `disconnect` | Client → Server | User leaves |
| `send_message` | Client → Server | Send chat message |
| `receive_message` | Server → Client | Broadcast message |
| `user_joined` | Server → Client | New user notification |
| `user_left` | Server → Client | User left notification |
| `typing` | Bidirectional | Typing indicators |
| `set_username` | Client → Server | Change username |

## 🔧 Configuration

### Server Settings (app.py)

```python
# Change server host/port
socketio.run(app, host='0.0.0.0', port=5000)

# Enable/disable debug mode
socketio.run(app, debug=True)

# Adjust message history limit
if len(message_history) > 100:  # Change limit here
    message_history.pop(0)
```

### Client Settings (index.html)

```javascript
// Change server connection
const socket = io('http://localhost:5000');

// Adjust typing timeout
typingTimeout = setTimeout(() => {
    // ... stop typing
}, 1000);  // Change timeout here
```

## 🎯 Learning Outcomes

### Computer Networks Concepts
- **TCP/IP Stack**: Understanding how WebSockets utilize TCP
- **Client-Server Model**: Request-response vs. persistent connections  
- **Real-time Protocols**: WebSocket vs. HTTP comparison
- **Event-driven Programming**: Asynchronous I/O handling

### Web Development Skills
- **Backend Development**: Flask framework and routing
- **Frontend Integration**: HTML5, CSS3, and JavaScript
- **API Design**: RESTful principles and WebSocket events
- **State Management**: Client-server state synchronization

## 🔬 Testing Multi-User Functionality

### Local Testing
1. Start the Flask server
2. Open multiple browser tabs to `http://localhost:5000`
3. Set different usernames in each tab
4. Send messages and observe real-time updates

### Network Testing
1. Find your local IP address: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Change server host to `0.0.0.0` in `app.py`
3. Other devices can connect to `http://YOUR_IP:5000`

### Load Testing
```bash
# Install testing tools
pip install websocket-client

# Create multiple connections
python -c "
import websocket
import threading

def test_connection():
    ws = websocket.WebSocketApp('ws://localhost:5000/socket.io/')
    ws.run_forever()

for i in range(10):
    threading.Thread(target=test_connection).start()
"
```

## 🚨 Troubleshooting

### Common Issues

**"ImportError: No module named 'flask_socketio'"**
```bash
pip install Flask-SocketIO
```

**"Address already in use"**
- Kill existing Flask processes
- Change port in `app.py`: `socketio.run(app, port=5001)`

**Messages not appearing**
- Check browser console for JavaScript errors
- Verify Socket.IO CDN is loading
- Ensure server is running

**WebSocket connection failed**
- Check firewall settings
- Verify server is accessible
- Try different browser

## 🚀 Enhancements & Extensions

### Possible Improvements
- **Database Integration**: SQLite/PostgreSQL for persistent chat history
- **User Authentication**: Login system with password protection
- **Private Messaging**: Direct messages between users
- **File Sharing**: Upload and share images/documents
- **Emoji Support**: Rich text formatting and emoji picker
- **Chat Rooms**: Multiple channels/rooms
- **Admin Features**: User moderation and message deletion
- **Deployment**: Docker containerization and cloud deployment

### Advanced Features
- **Video/Voice Chat**: WebRTC integration
- **End-to-end Encryption**: Secure message transmission
- **Bot Integration**: Automated responses and commands
- **Analytics Dashboard**: User activity and message statistics
- **Mobile App**: React Native or Flutter companion

## 📚 Technical References

- **Flask-SocketIO Documentation**: https://flask-socketio.readthedocs.io/
- **Socket.IO Client**: https://socket.io/docs/v4/client-api/
- **WebSocket Protocol (RFC 6455)**: https://tools.ietf.org/html/rfc6455
- **Flask Documentation**: https://flask.palletsprojects.com/

## 📝 Requirements

- **Python 3.7+**
- **Modern Web Browser** (Chrome, Firefox, Safari, Edge)
- **Network Connection** for multi-device testing

---

**🎉 Happy Chatting! 🚀**