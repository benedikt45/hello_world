from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('GET request, path:', self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if self.path == '/getPageWeather':
            data = {
                'buttons': [
                    {'value': 'Get weather',
                    'id': 'pushButton'}
                ],
                'text': [
                    {'name': 'inputCity'}
                ]
            }
            html = '<label for=''inputCity''>Введите интересуемый город:</label> \
				<input type=''text'' name=''inputCity''>\
				<button type=''submit''>GO</button>\
				<div id=''answer''>\
			    <div>'
            jsonData = json.dumps(data)
            #self.wfile.write(jsonData.encode('utf-8'))
            self.wfile.write(html.encode('utf-8'))
        #elif self.path == '/getWeather':
        #    self.wfile.write('currency'.encode('utf-8'))

    def do_POST(self):
        print('POST request, path:', self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if self.path == '/getWeather':
            city = self.rfile.read(int(self.headers['Content-Length']))
            #self.wfile.write('currency'.encode('utf-8'))


def start_server():
    server_address = ('localhost', 80)
    srv_inst = HTTPServer(server_address, ServerHandler)
    try:
        srv_inst.serve_forever()
    except KeyboardInterrupt:
        pass
    srv_inst.server_close()

if __name__=='__main__':
    start_server()