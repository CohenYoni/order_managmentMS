import sys
import sqlite3
import os
import json

outputJson = {'hadError':False, 'error':'', 'output':[]}
try:
    if len(sys.argv) != 2:
        raise Exception('You need to pass only one argument')
    DBlocation = sys.argv[1]
    tableName = 'products'
    if not os.path.isfile(DBlocation):
        raise Exception('Database does not exist (maybe you paseed wrong path as argument)')
    connectDB = sqlite3.connect(DBlocation)
    cursorDB = connectDB.cursor()
    records = cursorDB.execute('select * from ' + tableName + ';')
    outputJson['output'] = [{'prodName':prodName, 'price':output} for (prodName, output) in records.fetchall()]
    connectDB.close()
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = 'ERROR: ' + str(err) + '.'
finally:
    print(json.dumps(outputJson))
