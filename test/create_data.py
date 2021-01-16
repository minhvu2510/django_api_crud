from pymongo import MongoClient
client = MongoClient('mongodb://localhost/', 27017)
DATABASE = client.mvp
lst = ['contracts', 'marketing', 'warranties', 'business_planning', 'conferences', 'computers', 'office_technology']
def get_document(table,query,order=None,distinct=None,page=None,limit=None,incre=-1):
    if page:
        if not limit:
            limit = 20
        page = int(page)
        limit = int(limit)
        if order:
            res = DATABASE[table].find(query).sort(order, incre).skip((page-1)*limit).limit(limit)
        else:
            res = DATABASE[table].find(query).skip((page-1)*limit).limit(limit)
    else:
        if order:
            res = DATABASE[table].find(query).sort(order, incre)
        else:
            res = DATABASE[table].find(query)
    if distinct:
        res = res.distinct(distinct)
        res = filter(lambda r: r != '',res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return  message
def show_allcolection():
    allcolec = []
    for i in DATABASE.collection_names():
        allcolec.append(i)
    return allcolec
def get_all(table):
    res = DATABASE[table].find()
    res = filter(lambda r: r != '', res)
    if res:
        message = {"data": list(res)}
    else:
        message = {"data": []}
    return  message
if __name__ == '__main__':
    print(show_allcolection())