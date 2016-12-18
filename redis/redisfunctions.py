import redis

r_server = redis.Redis('localhost')    #this line creates a new Redis object and connects to our redis server
#r_server.set('test_key', 'test_value') #with the created redis object we can submits redis commands as its methods

#print 'previous set key ' + r_server.get('test_key')          # the previous set key is fetched
#print 'the counter was increased! '+ r_server.get('counter5') #notice that the key is increased now

# print r_server.incr('query.'+str(type)+"")   #we increase the key value by 1, has to be int


def getvarStatistics():
    return r_server.keys()

def getallStatistics():
    for key in r_server.scan_iter("counter1:*"):
      print key
    return '0' 

def getallStatistics():
    response = []
    for key in r_server.scan_iter():
        #print key, r_server.get(key) 
        response.append({'query': key, 'times': r_server.get(key)})
    return json.dumps(response)   

def getallStatistics2():
    for key in r_server.scan_iter():
        print key, r_server.get(key)    
    return '0'  
