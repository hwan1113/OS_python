import socketio

sio = socketio.AsyncClient()

@sio.event
async def message(data):
    print('I received a message!')
    
@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")
    
await sio.connect('http://localhost:5000')