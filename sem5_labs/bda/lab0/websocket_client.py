import asyncio
import websockets

async def handle_client(websocket, path):
    print("Client connected")
    try:
        # Send a message to the client
        await websocket.send("Hello, Client!")
        
        # Receive a message from the client
        message = await websocket.recv()
        print(f"Received message from client: {message}")
        
    except websockets.ConnectionClosedOK:
        print("Client disconnected")

async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("Server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_server())
