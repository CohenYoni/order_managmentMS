import sys
import json
import subprocess

outputJson = {'hadError':False, 'error':'', 'output':[]}
detailsJson={}
totalPrice = 0
try:
    if len(sys.argv) != 2:
        raise Exception('You need to pass only one argument')
    
    inputJson = json.loads(sys.argv[1].replace('\'', '"').replace('\\', '\\\\'))
    orderJson = inputJson['order']
    detailsJson['DBlocation']=inputJson['DBlocation']
    productsIDs=orderJson['productsIDs']
    
    for p in productsIDs:
        detailsJson['prodID'] = p
        outputFromGetPrice = json.loads(subprocess.check_output(['python', 'getPriceOfProdFromDB.py', json.dumps(detailsJson)], shell=True))
        
        if(outputFromGetPrice['hadError']==True):
            raise Exception(outputFromGetPrice['error'])
        
        JsonFromGetPrice=outputFromGetPrice['output']
        price=JsonFromGetPrice["price"]
        totalPrice = totalPrice + float(price)
    outputJson['output'] = totalPrice
        
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = str(err)
finally:
    print(json.dumps(outputJson))

