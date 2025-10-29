#!/usr/bin/env python3
"""
Simple TCP Chat Server
Allows one client to connect and chat with the server.
Type 'exit' to end the chat session.
"""

import socket
import sys

def start_server(host='localhost', port=12345):
    """Start the TCP chat server"""
    
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow socket reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind to address and port
        server_socket.bind((host, port))
        print(f"🌐 Server started on {host}:{port}")
        
        # Listen for connections (max 1 client)
        server_socket.listen(1)
        print("⏳ Waiting for client connection...")
        
        # Accept client connection
        client_socket, client_address = server_socket.accept()
        print(f"✅ Client connected from {client_address}")
        print("💬 Chat started! Type 'exit' to end the session.\n")
        
        # Chat loop
        while True:
            try:
                # Receive message from client
                message = client_socket.recv(1024).decode('utf-8')
                
                if not message or message.lower() == 'exit':
                    print("👋 Client disconnected.")
                    break
                
                print(f"Friend: {message}")
                
                # Get server response
                response = input("You: ")
                
                if response.lower() == 'exit':
                    print("👋 Ending chat session...")
                    client_socket.send(response.encode('utf-8'))
                    break
                
                # Send response to client
                client_socket.send(response.encode('utf-8'))
                
            except ConnectionResetError:
                print("🔌 Connection lost with client.")
                break
            except KeyboardInterrupt:
                print("\n🛑 Server interrupted by user.")
                break
    
    except Exception as e:
        print(f"❌ Server error: {e}")
    
    finally:
        # Close connections
        try:
            client_socket.close()
        except:
            pass
        server_socket.close()
        print("🔒 Server closed.")

if __name__ == "__main__":
    print("🚀 Starting TCP Chat Server...")
    print("=" * 40)
    start_server()