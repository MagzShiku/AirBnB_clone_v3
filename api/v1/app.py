from api.v1.views import app_views
from flask import Flask
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """
        a method to handle @app.teardown_appcontext that calls
        storage.close()
    """
    storage.close()


if __name__ == "__main__":
    """
        the main function:
        running Flask server (variable app) with
            - host = environment variable HBNB_API_HOST or 0.0.0.0
                if not defined
            - port = environment variable HBNB_API_PORT or 5000
                if not defined
            - threaded=True
    """
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
