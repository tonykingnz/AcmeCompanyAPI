import connexion
from datetime import datetime, timedelta
import logging

from connexion import NoContent

from exceptions import *

from service.store_service.store import *

#Store
def list(storeAddress=None):
    return (listStore(storeAddress))

def create(store):
    try:
        storeId = createStore(store)
        return (storeId, 201)
    except ApiCustomError as e:
        return ("Bad Request", 400)

def update(store, storeId):
    try:
        response = updateStore(store, storeId)
        return(response, 200)
    except ApiCustomError as e:
        return("Not found", 404)

#Configurations
logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('openapi.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
