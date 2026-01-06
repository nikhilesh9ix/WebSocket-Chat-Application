# 🌐 WebSocket Chat Application

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Socket.IO](https://img.shields.io/badge/SocketIO-5.3.6-black.svg)](https://socket.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, real-time web-based chat application built with **Flask-SocketIO** and **WebSockets**. This project demonstrates professional implementation of bidirectional client-server communication, event-driven architecture, and responsive web design.

> **Perfect for learning**: Computer Networks, WebSocket protocol, real-time communication, and full-stack web development!

## 📸 Screenshots

<div align="center">

### Chat Interface
![Chat Interface](docs/screenshots/chat-interface.png)
*Modern, responsive chat interface with real-time messaging*

### Multi-User Chat
![Multi-User Chat](docs/screenshots/multi-user.png)
*Multiple users chatting simultaneously with typing indicators*

</div>

## 🎯 Live Demo

### 🌐 **[Try Live Demo →](https://web-socket-chat-application.vercel.app/)**

Experience the real-time chat application in action! Open the link in multiple browser tabs to test multi-user functionality.

### Run Locally

Try it yourself:
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Start server: `python app.py`
4. Open `http://localhost:5000` in multiple tabs

**Quick Test**: Open 2-3 browser tabs and start chatting!

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Live Demo](#-live-demo)
- [Architecture](#️-architecture-overview)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Network Protocol Details](#-network-protocol-details)
- [Testing](#-testing-guide)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🔥 Core Functionality
- ✅ **Real-time Messaging** - Instant bidirectional communication using WebSockets
- ✅ **Multi-user Support** - Concurrent connections with individual session management
- ✅ **User Management** - Dynamic username assignment and modification
- ✅ **Message History** - Last 10 messages displayed to newly connected users
- ✅ **Typing Indicators** - Live typing status for enhanced UX
- ✅ **Connection Status** - Real-time join/leave notifications
- ✅ **Online User Counter** - Active user count display
- ✅ **Message Persistence** - In-memory storage of last 100 messages

### 🎨 UI/UX Features
- 🎨 **Modern Interface** - Clean, gradient-based responsive design
- 📱 **Mobile Responsive** - Optimized for desktop, tablet, and mobile
- 🎯 **Message Types** - Distinct styling for sent/received/system messages
- ⏰ **Timestamps** - Precise time tracking for all messages
- 📊 **Live Statistics** - User count, message count, and connection status
- 🔄 **Auto-scroll** - Automatic scroll to latest messages
- 💬 **Message Bubbles** - Chat-like message presentation

### 🔧 Technical Features
- ⚡ **Event-driven Architecture** - Asynchronous Socket.IO event handling
- 🛡️ **Error Handling** - Graceful connection failure management
- 🔒 **Input Validation** - Message sanitization and length limits
- 🌐 **CORS Support** - Cross-Origin Resource Sharing enabled
- 📡 **Broadcast System** - Efficient message distribution to all clients
- 🔄 **Reconnection Logic** - Automatic client reconnection on disconnection

## 🏗️ Architecture Overview

This project demonstrates key **Computer Networks** and **Software Engineering** concepts:

### Network Protocols
- **Transport Layer (TCP)**: WebSocket protocol built on reliable TCP connections
- **Application Layer**: HTTP/HTTPS for initial handshake, WebSocket for persistent communication
- **Full-Duplex Communication**: Bidirectional data flow without polling

### Design Patterns
- **Client-Server Architecture**: Centralized Flask backend serving multiple web clients
- **Event-Driven I/O**: Non-blocking asynchronous message handling
- **Publisher-Subscriber Pattern**: Broadcast messaging system
- **Session Management**: Per-client state tracking

### Technology Stack
**Backend:**
- Python 3.7+
- Flask 2.3.3 (Web framework)
- Flask-SocketIO 5.3.6 (WebSocket implementation)
- python-socketio 5.9.0

**Frontend:**
- HTML5
- CSS3 (Flexbox, Grid, Animations)
- JavaScript (ES6+)
- Socket.IO Client 4.0.0

## 📁 Project Structure

```
WebSocket-Chat-Application/
├── 📄 app.py                 # Main Flask-SocketIO backend server
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
├── 📁 templates/
│   └── 📄 index.html        # Frontend chat interface (HTML)
├── 📁 static/
│   └── 📄 style.css         # Responsive CSS styling
├── 📄 server.py             # Basic TCP chat server (legacy/educational)
└── 📄 client.py             # Basic TCP chat client (legacy/educational)
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with Socket.IO event handlers |
| `templates/index.html` | Frontend HTML with Socket.IO client integration |
| `static/style.css` | Modern responsive CSS with gradient styling |
| `server.py` | Simple TCP socket server (for learning TCP basics) |
| `client.py` | TCP socket client (demonstrates low-level networking) |
| `requirements.txt` | Python package dependencies |

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager) - Usually comes with Python
- A modern web browser (Chrome, Firefox, Safari, or Edge)

### Step 1: Clone the Repository

```bash
git clone https://github.com/nikhilesh9ix/WebSocket-Chat-Application.git
cd WebSocket-Chat-Application
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask 2.3.3
- Flask-SocketIO 5.3.6
- python-socketio 5.9.0
- python-engineio 4.7.1

### Step 4: Start the Server

```bash
python app.py
```

Expected output:
```
🚀 Starting Flask WebSocket Chat Server...
==================================================
🌐 Server will run on http://localhost:5000
💡 Open multiple browser tabs to test multi-user chat
==================================================
 * Running on http://0.0.0.0:5000
```

### Step 5: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

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

### Example Chat Session

**Browser Tab 1 (User: Alice):**
```
💬 ChatFlow
🟢 Connected | 👥 2 users online

System: Welcome to the chat, Alice!
System: Bob has joined the chat
Alice: Hello everyone!
Bob: Hi Alice! How's it going?
Alice: Great! This WebSocket chat is amazing.
```

**Browser Tab 2 (User: Bob):**
```
💬 ChatFlow
🟢 Connected | 👥 2 users online

System: Welcome to the chat, Bob!
Alice: Hello everyone!
Bob: Hi Alice! How's it going?
Alice: Great! This WebSocket chat is amazing.
Bob is typing...
```

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

### Environment Variables

Create a `.env` file for production deployments:

```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
HOST=0.0.0.0
PORT=5000
DEBUG=False
```

### Server Settings (app.py)

```python
# Change server host/port
socketio.run(app, host='0.0.0.0', port=5000)

# Enable/disable debug mode (set False in production)
socketio.run(app, debug=True)

# Adjust message history limit
if len(message_history) > 100:  # Change limit here
    message_history.pop(0)

# Configure CORS for production
socketio = SocketIO(app, cors_allowed_origins=["https://yourdomain.com"])
```

### Client Settings (index.html)

```javascript
// Change server connection URL
const socket = io('http://localhost:5000');

// For production
const socket = io('https://yourdomain.com');

// Adjust typing indicator timeout
typingTimeout = setTimeout(() => {
    // Stop typing indicator
}, 1000);  // Change timeout here (milliseconds)
```

### Message Limits

Adjust in respective files:
- **Message length**: 500 characters (index.html - maxlength attribute)
- **History size**: 100 messages (app.py - message_history list)
- **Username length**: 20 characters (index.html - maxlength attribute)

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

### Computer Networks Concepts
- ✅ **TCP/IP Stack**: WebSocket protocol built on TCP for reliable communication
- ✅ **OSI Model**: Application Layer (HTTP/WebSocket) and Transport Layer (TCP)
- ✅ **Client-Server Architecture**: Centralized server managing multiple clients
- ✅ **Full-Duplex Communication**: Bidirectional real-time data flow
- ✅ **Protocol Upgrade**: HTTP to WebSocket handshake mechanism
- ✅ **Event-driven Architecture**: Non-blocking asynchronous I/O

### Web Development Skills
- ✅ **Backend Development**: Flask framework, routing, and session management
- ✅ **Frontend Integration**: Responsive HTML5, CSS3, and vanilla JavaScript
- ✅ **WebSocket API**: Socket.IO implementation for real-time features
- ✅ **State Management**: Synchronizing client and server state
- ✅ **Error Handling**: Connection failures and disconnection management
- ✅ **UI/UX Design**: Modern responsive interface with animations

## 🧪 Testing Guide

### Local Multi-User Testing

1. **Start the server**
   ```bash
   python app.py
   ```

2. **Open multiple browser tabs/windows**
   - Navigate to `http://localhost:5000` in each
   - Use different browsers if needed (Chrome, Firefox, Edge)

3. **Set unique usernames** in each tab

4. **Test features:**
   - Send messages from different tabs
   - Observe real-time message delivery
   - Check typing indicators
   - Monitor user join/leave notifications
   - Verify user count updates

### Network Testing (Multiple Devices)

1. **Find your local IP address:**
   
   **Windows:**
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)
   
   **macOS/Linux:**
   ```bash
   ifconfig | grep "inet "
   # or
   ip addr show
   ```

2. **Ensure server listens on all interfaces** (already configured):
   ```python
   socketio.run(app, host='0.0.0.0', port=5000)
   ```

3. **Connect from other devices** on the same network:
   ```
   http://YOUR_LOCAL_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

4. **Configure firewall** if needed:
   - Allow incoming connections on port 5000
   - Windows: `Windows Defender Firewall > Allow an app`
   - Linux: `sudo ufw allow 5000`

### Automated Testing

**Basic Connection Test:**
```python
# test_connection.py
import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')
    sio.emit('send_message', {'message': 'Test message'})

@sio.on('receive_message')
def on_message(data):
    print(f"Received: {data}")
    sio.disconnect()

sio.connect('http://localhost:5000')
sio.wait()
```

**Run the test:**
```bash
pip install python-socketio[client]
python test_connection.py
```

### Browser Console Testing

Open browser DevTools (F12) and test Socket.IO events:

```javascript
// Send a message
socket.emit('send_message', {message: 'Test from console'});

// Change username
socket.emit('set_username', {username: 'ConsoleUser'});

// Check connection
console.log(socket.connected);  // Should be true
```

## 🚨 Troubleshooting

### Common Issues

#### Installation Problems

**Problem:** `ImportError: No module named 'flask_socketio'`

**Solution:**
```bash
# Install all required packages
pip install -r requirements.txt

# Or install individually
pip install Flask-SocketIO python-socketio
```

**Problem:** `ModuleNotFoundError: No module named 'eventlet'`

**Solution:**
```bash
# Install eventlet (optional but recommended for better performance)
pip install eventlet
```

#### Server Issues

**Problem:** `OSError: [Errno 48] Address already in use`

**Solutions:**

**Windows:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace <PID> with actual process ID)
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
# Find and kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use fuser
fuser -k 5000/tcp
```

**Alternative:** Change port in [app.py](app.py):
```python
socketio.run(app, port=5001)  # Use different port
```

**Problem:** Server starts but can't access from browser

**Solutions:**
- ✅ Verify server is running on `http://0.0.0.0:5000` (not `127.0.0.1`)
- ✅ Try both `http://localhost:5000` and `http://127.0.0.1:5000`
- ✅ Check Windows Firewall or antivirus blocking port 5000
- ✅ Ensure no other service is using port 5000
- ✅ Check browser console (F12) for JavaScript errors

#### Connection Issues

**Problem:** WebSocket connection fails in browser console

**Solutions:**

1. **Check browser console for errors** (Press F12)
   ```
   WebSocket connection to 'ws://localhost:5000/socket.io/' failed
   ```

2. **Verify Socket.IO CDN is loading:**
   - Open Network tab in DevTools
   - Look for `socket.io.js` (should be status 200)
   - If 404/blocked, check internet connection

3. **Ensure server is running:**
   ```bash
   # You should see this output
   🚀 Starting Flask WebSocket Chat Server...
   * Running on http://0.0.0.0:5000
   ```

4. **Try different browser:**
   - Chrome/Edge (recommended)
   - Firefox
   - Safari (macOS)

5. **Clear browser cache:**
   - Chrome: Ctrl+Shift+Del → Clear cached images and files
   - Firefox: Ctrl+Shift+Del → Cached Web Content

**Problem:** Messages not appearing in real-time

**Solutions:**
- ✅ Check connection status indicator (should show "Connected")
- ✅ Open browser console and look for JavaScript errors
- ✅ Verify Socket.IO client/server version compatibility
- ✅ Check Network tab for failed WebSocket frames
- ✅ Ensure server logs show message events

#### Network/Firewall Issues

**Problem:** Can't connect from other devices on the same network

**Solutions:**

1. **Verify server binding:**
   ```python
   # In app.py - should be 0.0.0.0, not localhost
   socketio.run(app, host='0.0.0.0', port=5000)
   ```

2. **Find your local IP address:**
   
   **Windows:**
   ```bash
   ipconfig
   # Look for "IPv4 Address" (e.g., 192.168.1.100)
   ```
   
   **macOS/Linux:**
   ```bash
   ifconfig | grep "inet "
   # Or
   ip addr show
   ```

3. **Configure Windows Firewall:**
   - Open Windows Defender Firewall
   - Click "Allow an app or feature"
   - Click "Allow another app"
   - Add Python executable
   - Enable both "Private" and "Public" networks

4. **Test with firewall disabled** (temporarily):
   ```bash
   # Windows - Disable temporarily to test
   netsh advfirewall set allprofiles state off
   
   # Re-enable after testing
   netsh advfirewall set allprofiles state on
   ```

5. **Ensure same network:**
   - Both devices must be on the same WiFi/LAN
   - Check subnet masks match (usually 255.255.255.0)

6. **Connect from other device:**
   ```
   http://YOUR_LOCAL_IP:5000
   Example: http://192.168.1.100:5000
   ```

#### Browser-Specific Issues

**Problem:** Application doesn't work in older browsers

**Solution:** Ensure browser supports:
- ✅ WebSocket API
- ✅ ES6 JavaScript (const, let, arrow functions)
- ✅ Modern CSS (Flexbox, Grid)
- ✅ Fetch API

**Minimum browser versions:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Opera 76+

**Problem:** CORS errors in browser console

**Solution:**
```python
# In app.py - for development only
socketio = SocketIO(app, cors_allowed_origins="*")

# For production - specify your domain
socketio = SocketIO(app, cors_allowed_origins=["https://yourdomain.com"])
```

### Debug Mode

Enable detailed logging to diagnose issues:

**In [app.py](app.py):**
```python
# Enable Socket.IO logging
socketio = SocketIO(app, 
    cors_allowed_origins="*", 
    logger=True,           # Enable Socket.IO logging
    engineio_logger=True   # Enable Engine.IO logging
)

# Run with debug mode
socketio.run(app, debug=True)
```

**Check server logs for:**
- Connection events: "🟢 User_xxx connected"
- Message events: "💬 Username: message"
- Disconnection events: "🔴 User_xxx disconnected"
- Error messages and stack traces

### Still Having Issues?

If problems persist:

1. **Check project issues**: [GitHub Issues](https://github.com/nikhilesh9ix/WebSocket-Chat-Application/issues)
2. **Create new issue** with:
   - Operating system and version
   - Python version (`python --version`)
   - Browser and version
   - Error messages (full stack trace)
   - Steps to reproduce
3. **Include relevant logs** from both server and browser console

## 🚀 Deployment

### Docker Deployment

**1. Create Dockerfile:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

**2. Create docker-compose.yml:**

```yaml
version: '3.8'

services:
  websocket-chat:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=${SECRET_KEY}
    restart: unless-stopped
```

**3. Build and run:**

```bash
docker-compose up -d
```

### Cloud Deployment Options

#### Heroku

**1. Create Procfile:**
```
web: python app.py
```

**2. Deploy:**
```bash
heroku create your-app-name
git push heroku master
heroku open
```

#### AWS EC2

**1. Launch EC2 instance** (Ubuntu 20.04 LTS recommended)

**2. Install dependencies:**
```bash
sudo apt update
sudo apt install python3-pip python3-venv
```

**3. Clone and setup:**
```bash
git clone https://github.com/nikhilesh9ix/WebSocket-Chat-Application.git
cd WebSocket-Chat-Application
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**4. Run with gunicorn:**
```bash
pip install gunicorn eventlet
gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 app:app
```

**5. Setup Nginx reverse proxy** (recommended for production)

#### Azure Web Apps

**1. Create Web App** in Azure Portal

**2. Configure deployment:**
```bash
az webapp up --name your-app-name --resource-group your-group
```

**3. Set environment variables** in Azure Portal

### Production Considerations

⚠️ **Important for Production:**

1. **Change SECRET_KEY** in app.py to a secure random string
2. **Disable debug mode**: `socketio.run(app, debug=False)`
3. **Use HTTPS**: Configure SSL/TLS certificates
4. **Set CORS properly**: Restrict origins to your domain
5. **Use production WSGI server**: Gunicorn with eventlet/gevent
6. **Add rate limiting**: Prevent message spam
7. **Implement authentication**: User login system
8. **Use external database**: Redis or PostgreSQL for persistence
9. **Set up monitoring**: Application logging and error tracking
10. **Configure firewall**: Only allow necessary ports

## 🔮 Future Enhancements

### Planned Features
- 🗄️ **Database Integration**: PostgreSQL/MongoDB for persistent chat history
- 🔐 **User Authentication**: JWT-based login/registration system
- 💬 **Private Messaging**: Direct messages between users
- 📁 **File Sharing**: Image and document upload functionality
- 😊 **Emoji Support**: Rich text formatting and emoji picker
- 🏠 **Chat Rooms**: Multiple channels/topics
- 👮 **Admin Panel**: User moderation and message management
- 🔔 **Notifications**: Browser push notifications for new messages

### Advanced Features
- 📹 **Video/Voice Chat**: WebRTC integration for multimedia communication
- 🔒 **End-to-End Encryption**: Secure message transmission
- 🤖 **Bot Integration**: Automated responses and slash commands
- 📱 **Mobile App**: React Native or Flutter companion apps
- 🌍 **Internationalization**: Multi-language support
- 📊 **Analytics Dashboard**: User activity and statistics

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** with clear, documented code
4. **Test thoroughly** on multiple browsers
5. **Commit your changes**: `git commit -m "Add: amazing feature"`
6. **Push to your fork**: `git push origin feature/amazing-feature`
7. **Open a Pull Request** with a clear description

### Contribution Guidelines
- 📝 Write clear commit messages
- 🧪 Test your code thoroughly
- 📚 Update documentation as needed
- 🎨 Maintain consistent code style
- 🐛 Report bugs with detailed reproduction steps

## 📚 Technical References

### Official Documentation
- **Flask**: https://flask.palletsprojects.com/
- **Flask-SocketIO**: https://flask-socketio.readthedocs.io/
- **Socket.IO**: https://socket.io/docs/v4/
- **WebSocket Protocol (RFC 6455)**: https://tools.ietf.org/html/rfc6455

### Learning Resources
- **Real-Time Communication**: https://web.dev/websockets-basics/
- **Flask Mega-Tutorial**: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- **Socket.IO Chat Tutorial**: https://socket.io/get-started/chat

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) file for details.

## 👤 Author

**Nikhilesh**
- GitHub: [@nikhilesh9ix](https://github.com/nikhilesh9ix)
- Repository: [WebSocket-Chat-Application](https://github.com/nikhilesh9ix/WebSocket-Chat-Application)

## 🙏 Acknowledgments

- Flask and Socket.IO teams for excellent frameworks
- Open source community for inspiration and resources
- All contributors who help improve this project

---

<div align="center">

### 🌟 If you find this project helpful, please star it! 🌟

**Made with ❤️ and ☕ by Nikhilesh**

[Report Bug](https://github.com/nikhilesh9ix/WebSocket-Chat-Application/issues) · 
[Request Feature](https://github.com/nikhilesh9ix/WebSocket-Chat-Application/issues) · 
[Contribute](https://github.com/nikhilesh9ix/WebSocket-Chat-Application/pulls)

**Happy Chatting! 🚀💬**

</div>