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
    
    for (ordID, custName, custPhone, ordDate) in orders:
        records = cursorDB.execute('SELECT productID FROM {0} WHERE ordID={1};'.format(itemsOfOrdersTableName, ordID))
        itemsOfOrder = []
        for rec in records.fetchall():
            itemsOfOrder.extend([id for id in rec])
        outputJson['output'].append(
                                        {
                                            'ordID':ordID,
                                            'custName':custName,
                                            'custPhone':custPhone,
                                            'ordDate':ordDate,
                                            'productsIDs':itemsOfOrder
                                        }
                                    )
                            
    connectDB.close()
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = 'ERROR: ' + str(err) + '.'
finally:
    print(json.dumps(outputJson))
