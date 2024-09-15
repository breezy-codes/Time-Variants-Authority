import http.server
import logging
import os
from datetime import datetime

# Configuration
LOG_FILE = 'access.log'
TRACKING_PIXEL = 'pixel.gif'
PORT = 80

# Function to create the tracking pixel if it doesn't exist
def create_tracking_pixel():
    if not os.path.exists(TRACKING_PIXEL):
        print(f"Creating {TRACKING_PIXEL}...")
        os.system(f"convert -size 1x1 xc:none {TRACKING_PIXEL}")

# HTTP request handler class
class TrackingHandler(http.server.SimpleHTTPRequestHandler):
    def custom_log_request(self):
        # Log the request details
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent')
        log_entry = f"{datetime.now()} - IP: {client_ip} - User-Agent: {user_agent}"
        logging.info(log_entry)
        print(log_entry)  # Print to console as well

    def do_GET(self):
        # Log request when pixel is accessed
        self.custom_log_request()

        # Serve the tracking pixel (GIF image)
        if self.path == f'/{TRACKING_PIXEL}':
            self.send_response(200)
            self.send_header('Content-type', 'image/gif')
            self.end_headers()
            with open(TRACKING_PIXEL, 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()

def display_title():
    print(r"""
██████╗ ██╗██╗  ██╗███████╗██╗     ██╗███████╗██╗   ██╗
██╔══██╗██║╚██╗██╔╝██╔════╝██║     ██║██╔════╝╚██╗ ██╔╝
██████╔╝██║ ╚███╔╝ █████╗  ██║     ██║█████╗   ╚████╔╝ 
██╔═══╝ ██║ ██╔██╗ ██╔══╝  ██║     ██║██╔══╝    ╚██╔╝  
██║     ██║██╔╝ ██╗███████╗███████╗██║██║        ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝        ╚═╝   
""")


# Main function to start the server
def start_server():
    display_title()
    # Configure logging
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
    print(f"Logging to {LOG_FILE}...")

    # Create the tracking pixel if not already present
    create_tracking_pixel()

    # Start the HTTP server
    server_address = ('0.0.0.0', PORT)
    httpd = http.server.HTTPServer(server_address, TrackingHandler)
    print(f"Starting server on port {PORT}...")
    httpd.serve_forever()

if __name__ == '__main__':
    start_server()
