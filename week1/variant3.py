from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

def run(server_class=HTTPServer, handler_class=MyHttpRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    # 現在のディレクトリをWebサーバーのルートディレクトリとして設定
    os.chdir('./')  # 必要に応じて、静的ファイルが格納されているディレクトリへのパスを指定
    run()