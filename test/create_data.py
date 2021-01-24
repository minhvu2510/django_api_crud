from pymongo import MongoClient
import requests
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
def create_data():
    url = "http://127.0.0.1:81/disable-drive"
    headers = {
        'Authorization': 'af4593ff029c48db8abc4363803278da',
        'Content-Type': 'application/json'
    }
    data = {
        'drive_id': drive_id
    }
    response = requests.post(url, data=data, headers=headers, timeout=7)
    query = {}
    for word in get_document(get_document('contracts', query)):
        print(word)
if __name__ == '__main__':
    # query = {}
    # print(get_document('contracts', query))
    create_data()