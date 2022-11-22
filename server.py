from http.server import BaseHTTPRequestHandler
import logging
import os
import state

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        if self.path == '/':
            self.path = '/index.html'

        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
                print("jsadask")
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)
    
    def do_Post(self):
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        if self.path == '/on':
            if state.CURRENT_STATE == 0 : 
                state.CURRENT_STATE = 1
                self.send_response(200, 'Turned ON')
        if self.path == '/of':
            if state.CURRENT_STATE == 1 : state.CURRENT_STATE = 0
