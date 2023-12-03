#!/usr/bin/python3
"""
starting my api
"""


from api.v1.views import app_views


@app_views.route("/status", methods=["GET"])
def get_status():
    """
    create a route /status on the object app_views that
    returns a JSON: "status": "OK"
    """
    return {"status": "OK"}
