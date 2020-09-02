import connexion
import logging
from connexion import NoContent

def listStore():
    return NoContent
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
