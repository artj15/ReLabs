import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
num = 0

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
        <link href="{{ url_for('static', path = '/styles.css') }}" rel="stylesheet">
    </head>
    <body>
        <h1>WebSocket Chat</h1>

        <ul id='messages'>
        </ul>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                console.log(event.data)
                message.appendChild(document.createTextNode(event.data.match(/\D+/)))
                messages.appendChild(message)
                message.appendChild(document.createTextNode(event.data.match(/\d+/)[0]))
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    global num
    num = 0
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global num
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        num += 1
        if len(data) == 0:
            data = ' '
        #await websocket.send_text(f"{data} {str(num)}")#, websocket.send_text()
        await websocket.send_json(data + ' ' + str(num))



if __name__ == '__main__':
    uvicorn.run(app)