from wsgiref.simple_server import make_server

from FastFramework.Application import Application
from FastFramework.Controller import HomeController

import sys

app = Application()
app.new_route("/", "GET", HomeController.home)


if __name__ == "__main__":
    try:
        server = make_server("127.0.0.1", 8000, app)
        server.serve_forever()
    except KeyboardInterrupt:
        # quit
        sys.exit()