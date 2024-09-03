import asyncio
import websockets

async def start_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Receive a message from the server
        message = await websocket.recv()
        print(f"Received from server: {message}")
        
        # Send a message to the server
        await websocket.send("Hello, Server!")

if __name__ == "__main__":
    asyncio.run(start_client())
