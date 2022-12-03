from typing import Callable, Optional


class Application:
    def __init__(self):
        self._route = {}

    def __call__(self, environnement, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])

        method = environnement["REQUEST_METHOD"].upper()
        path = environnement["PATH_INFO"]

        if method not in self._route:
            content = "<h1>Method not supported</h1>"
        elif path not in self._route[method]:
            content = "<h1>Route not found</h1>"
        else:
            content = self._route[method][path]()

        return [content.encode()]

    def new_route(self, route: str, method: str, callback: Callable | str, route_name: Optional[str] = None) -> None:
        method = method.upper()
        if method not in self._route:
            self._route[method] = {}

        if route in self._route[method]:
            raise Exception(f"Route {route} already found")

        self._route[method][route] = callback

    def initialize(self):
        pass
