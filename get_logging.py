import asyncio
import websockets


async def get_logs_ws(level="debug"):
    async with websockets.connect('ws://127.0.0.1:9090/logs?level=%s&token=' % level, ping_interval=None) as websocket:
        # await websocket.send("Jimmy")
        # print(f"(client) send to server: Jimmy")
        print("涅的")
        while True:
            name = await websocket.recv()

            print(f"{name}")

            file_path = 'file.txt'  # choose your file path
            with open(file_path, "a") as output_file:
                output_file.write(name)

asyncio.get_event_loop().run_until_complete(
        get_logs_ws(level='debug'))

# if __name__ == '__main__':
#
#     asyncio.get_event_loop().run_until_complete(
#         get_logs_ws(level='debug'))

