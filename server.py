import socketserver


clients = []

class ChatHandler(socketserver.BaseRequestHandler):
  
    def handle(self):
        global clients
        
        clients.append(self.request)
        print(f"New connection from: {self.client_address}")

        while True:
            
            message = self.request.recv(1024)
            if not message:
                
                 print(f"Received message: {message.decode()} from {self.client_address}")
                
        
            for client in clients:
                if client != self.request:
                    client.sendall(message)
        
        
        clients.remove(self.request)
        print(f"Disconnected: {self.client_address}")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    print(f"Server starting on {HOST}:{PORT}")

    
    with socketserver.ThreadingTCPServer((HOST, PORT), ChatHandler) as server:
        server.serve_forever()
