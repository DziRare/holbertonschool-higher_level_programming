#!/usr/bin/python3
"""This module runs a simple API built with the http.server module."""
import http.server
import json

PORT = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """This handler class answers GET requests for each endpoint."""

    def _send(self, code, body, content_type="text/plain"):
        """This function sends a response with a status, body and type."""
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, code, obj):
        """This function sends a Python object as a JSON response."""
        self._send(code, json.dumps(obj), "application/json")

    def do_GET(self):
        """This function routes GET requests to the matching endpoint."""
        if self.path == "/":
            self._send(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30,
                                  "city": "New York"})
        elif self.path == "/status":
            self._send(200, "OK")
        elif self.path == "/info":
            self._send_json(200, {"version": "1.0",
                                  "description":
                                  "A simple API built with http.server"})
        else:
            self._send(404, "Endpoint not found")


def run(port=PORT):
    """This function starts the HTTP server on the given port."""
    server = http.server.HTTPServer(("", port), SimpleAPIHandler)
    print(f"Serving on port {port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
