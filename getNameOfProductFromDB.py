import sys
import sqlite3
import os
import json

outputJson = {'hadError':False, 'error':'', 'output':{}}
try:
    if len(sys.argv) != 2:
        raise Exception('You need to pass only one argument')
    inputJson = json.loads(sys.argv[1].replace('\'', '"').replace('\\', '\\\\'))
    DBlocation = inputJson['DBlocation']
    prodID = inputJson['prodID']
    tableName = 'products'
    if not os.path.isfile(DBlocation):
        raise Exception('Database does not exist (maybe you paseed wrong path as argument)')
    if type(prodID) != int:
        raise Exception('product ID must be a number')
    connectDB = sqlite3.connect(DBlocation)
    cursorDB = connectDB.cursor()
    record = cursorDB.execute('SELECT prodName FROM {0} WHERE prodID={1};'.format(tableName, prodID))
    prodName = record.fetchall()
    if prodName == []:
        raise Exception('There is no product with #ID ' + str(prodID))
    outputJson['output'] = {'prodName':prodName}
    connectDB.close()
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = 'ERROR: ' + str(err) + '.'
finally:
    print(json.dumps(outputJson))
