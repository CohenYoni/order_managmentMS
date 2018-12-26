import sys
import sqlite3
import os
import json

outputJson = {'hadError':False, 'error':'', 'output':[]}
try:
    if len(sys.argv) != 2:
        raise Exception('You need to pass only one argument')
    DBlocation = sys.argv[1]
    ordersTableName = 'orders'
    itemsOfOrdersTableName = 'itemsOfOrder'
    productsTableName = 'products'
    if not os.path.isfile(DBlocation):
        raise Exception('Database does not exist (maybe you paseed wrong path as argument)')
    connectDB = sqlite3.connect(DBlocation)
    cursorDB = connectDB.cursor()
    records = cursorDB.execute('SELECT * FROM {0};'.format(ordersTableName))
    orders = records.fetchall()
    records = cursorDB.execute('SELECT i.ordID, p.prodName FROM {0} as p, {1} as i WHERE p.prodID=i.productID;'.format(productsTableName, itemsOfOrdersTableName))
    itemsOfOrders = records.fetchall()
    
    outputJson['output'] = [
                            {
                                'ordID':ordID,
                                'custName':custName,
                                'custPhone':custPhone,
                                'ordDate':ordDate,
                                'productsNames':[
                                    prodName for (itemOrdID, prodName) in itemsOfOrders if itemOrdID == ordID
                                    ]
                                } for (ordID, custName, custPhone, ordDate) in orders
                            ]
    connectDB.close()
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = 'ERROR: ' + str(err) + '.'
finally:
    print(json.dumps(outputJson))
