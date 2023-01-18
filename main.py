#Handler for the GET requests
def do_GET(self):
    if self.path=="/":
        self.path="/home.html"

    if self.path=="/command/":
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("transfer +79000000000")
        self.wfile.write("transfer +89000000000")
        self.wfile.write("transfer +90000000")
        return