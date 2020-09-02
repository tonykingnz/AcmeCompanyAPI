import psycopg2


def list(name, address, pageSize, pageIndex, orderBy):
    connection = psycopg2.connect(user = "postgres", password = "postgres", host = "0.0.0.0", port = "5432", database = "acme_db")
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
    content = []
    for item in rs:
        content[i] = rs.resolve()
    lastPage = true
    if content.size > pageSize:
        lastPage = false
        content.removeLastElement()
    return PageList(content, pageSize, pageIndex. lastPage)
