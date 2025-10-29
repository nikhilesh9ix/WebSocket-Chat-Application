#!/usr/bin/env python3
"""
Simple TCP Chat Client
Connects to the chat server and allows real-time messaging.
Type 'exit' to end the chat session.
"""

import socket
import sys

def start_client(host='localhost', port=12345):
    """Connect to the TCP chat server"""
    
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to server
        print(f"🔗 Connecting to server at {host}:{port}...")
        client_socket.connect((host, port))
        print("✅ Connected to server!")
        print("💬 Chat started! Type 'exit' to end the session.\n")
        
        # Chat loop
        while True:
            try:
                # Get user message
                message = input("You: ")
                
                if message.lower() == 'exit':
                    print("👋 Ending chat session...")
                    client_socket.send(message.encode('utf-8'))
                    break
                
                # Send message to server
                client_socket.send(message.encode('utf-8'))
                
                # Receive response from server
                response = client_socket.recv(1024).decode('utf-8')
                
                if not response or response.lower() == 'exit':
                    print("👋 Server ended the chat session.")
                    break
                
                print(f"Friend: {response}")
                
            except ConnectionResetError:
                print("🔌 Connection lost with server.")
                break
            except KeyboardInterrupt:
                print("\n🛑 Chat interrupted by user.")
                break
    
    except ConnectionRefusedError:
        print(f"❌ Could not connect to server at {host}:{port}")
        print("💡 Make sure the server is running first!")
    except Exception as e:
        print(f"❌ Client error: {e}")
    
    finally:
        # Close connection
        client_socket.close()
        print("🔒 Client disconnected.")

if __name__ == "__main__":
    print("🚀 Starting TCP Chat Client...")
    print("=" * 40)
    start_client()