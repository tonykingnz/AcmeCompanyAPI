import connexion
import logging
from connexion import NoContent

from exceptions import *

from storeService import list

def listStore(nameTerm, addressTerm, pageSize, pageIndex, orderBy):
    try: 
        response = list(nameTerm, addressTerm, pageSize, pageIndex, orderBy)
        return (response, 200)
    except APICustomError as e:
        return ("bad request", 400)

def addStore():
    return NoContent
def updateStore():
    return NoContent
def listStoreItems():
    return NoContent
def addStoreItem():
    return NoContent
def addStoreOrder():
    return NoContent

logging.basicConfig(level=logging.INFO)

app = connexion.App(__name__)
app.add_api('openapi.yaml')
app.run(port=8080)

#application = app.app

#if __name__ == '__main__':
    # run our standalone gevent server
    #app.run(port=8080, server='gevent')
