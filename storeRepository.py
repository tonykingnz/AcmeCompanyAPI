import psycopg2


def list(name, address, pageSize, pageIndex, orderBy):
    connection = psycopg2.connect(user = "#####", password = "*****", host = "127.0.0.1", port = "5432", database = "acme_db")
    rs = connection.query("""
        select 
            * 
        from 
            store 
        where 
            (${name} is null or name like ${name}||'%')
            and 
            (${address} is null or name like ${address}||'%')
            and
            (${storeId} is null or storeId = ${storeId})
        limit ${pageSize} + 1 offset ${pageIndex} * ${pageSize}
    """)
    conteudo = []
    for item in rs:
        conteudo[i] = rs.resolve()
    lastPage = true
    if conteudo.size > pageSize:
        lastPage = false
        conteudo.removeLastElement()
    return PageList(conteudo, pageSize, pageIndex. lastPage)
