import storeRepository

def list(name, address, pageSize=20, pageIndex=1, orderBy='name asc'):
    return storeRepository.list(name, address, pageSize, pageIndex, orderBy)
