from pymongo import MongoClient
import requests
import time
client = MongoClient('mongodb://localhost/', 27017)
DATABASE = client.mvp
lst = ['marketing', 'warranties', 'business_planning', 'conferences', 'computers', 'office_technology','electronics', 'regulations', 'correspondence',
       'computers', 'shopping', 'marketing', 'inventory', 'storage', 'hiring_and_training']
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
def create_topic():
    # url = "http://127.0.0.1:8000/topics"
    url = "https://toeic-essential-staging.herokuapp.com/topics"
    headers = {
        'Authorization': 'ec8f40cd6b7106f59475ff0a5f72e29c6dfc19b5'
    }
    for topic in lst:
        param = {'topic': topic}
        response = requests.post(url, data=param, headers=headers, timeout=17)
        print(response)
        time.sleep(1)
def create_words():
    url = "http://127.0.0.1:8000/words"
    headers = {
        'Authorization': 'af4593ff029c48db8abc4363803278da'
    }
    query = {}
    contrac = get_document('contracts', query)['data']
    print(contrac[-1])
    for toipic in lst:
        for word in contrac:
            print(word['key'], word['value'])
            param = {'word': word['key'],
                     'mean': word['value'],


                     'topic': toipic
                     }
            response = requests.post(url, data=param, headers=headers, timeout=17)
            print(response)
            time.sleep(1)
    # for topic in lst:
    #     param = {'topic': topic}
    #     response = requests.post(url, data=param, headers=headers, timeout=17)
    #     print(response)
def create_topic():
    # url = "http://127.0.0.1:8000/topics"
    url = "https://toeic-essential-staging.herokuapp.com/topics"
    headers = {
        'Authorization': 'Token ec8f40cd6b7106f59475ff0a5f72e29c6dfc19b5'
    }
    query = {}
    contrac = get_document('contracts', query)['data']
    # print(contrac[-1])
    for toipic in lst:
        param = {'level': 10,
                 'topic': toipic
                 }
        response = requests.post(url, data=param, headers=headers, timeout=17)
        print(response)
        # time.sleep(1)
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
def create_words():
    url = "http://127.0.0.1:8000/words"
    headers = {
        'Authorization': 'af4593ff029c48db8abc4363803278da'
    }
    query = {}
    contrac = get_document('contracts', query)['data']
    print(contrac[-1])
    for toipic in lst:
        for word in contrac:
            print(word['key'], word['value'])
            param = {'word': word['key'],
                     'mean': word['value'],
                     'topic': toipic
                     }
            response = requests.post(url, data=param, headers=headers, timeout=17)
            print(response)
            time.sleep(1)
    # for topic in lst:
    #     param = {'topic': topic}
    #     response = requests.post(url, data=param, headers=headers, timeout=17)
    #     print(response)

if __name__ == '__main__':
    # create_data()
    # print(show_allcolection())
    # query = {}
    # print(get_document('contracts', query)['data'])
    print(create_topic())
    # print(create_words())
