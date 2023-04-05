import asyncio
import websockets
async def test():
    async with websockets.connect('wss://localhost:997') as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print(response)
asyncio.get_event_loop().run_until_complete(test())