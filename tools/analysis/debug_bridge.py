import socket, threading, json, time
from http.server import HTTPServer, BaseHTTPRequestHandler
client = None
reader = None
lock = threading.Lock()
counter = 0

def accept():
    global client, reader
    listener = socket.socket()
    listener.bind(('127.0.0.1', 58991))
    listener.listen(1)
    while True:
        connection, _ = listener.accept()
        with lock:
            client = connection
            client.settimeout(10)
            reader = client.makefile('rb')

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        global counter
        request = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        output=[]
        try:
            with lock:
                if client is None: raise RuntimeError('DOSBox debugger not connected')
                for command in request['commands']:
                    counter += 1
                    client.sendall(f'REQ {counter} {command}\n'.encode())
                    lines=[]
                    while True:
                        line=reader.readline().decode(errors='replace').rstrip()
                        if not line: raise RuntimeError('Empty protocol line or disconnected')
                        lines.append(line)
                        if line == f'END {counter}': break
                    output.append(lines)
            result={'ok':True, 'output':output}
        except Exception as e:
            result={'ok':False,'error':str(e),'output':output}
        data=json.dumps(result).encode()
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    def log_message(self,*args): pass

threading.Thread(target=accept,daemon=True).start()
HTTPServer(('127.0.0.1',58992),Handler).serve_forever()
