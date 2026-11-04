"""Production entry point: serves the Flask app under /api.

Firebase Hosting forwards /api/** to Cloud Run, so the browser sees one site.
Local development (flask run) does not use this file, so routes stay at /.
"""
from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from backend.app import app as flask_app

application = DispatcherMiddleware(NotFound(), {"/api": flask_app})
