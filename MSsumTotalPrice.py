import sys
import json
import subprocess

outputJson = {'hadError':False, 'error':'', 'output':[]}
totalPrice = 0
try:
    if len(sys.argv) != 2:
        raise Exception('You need to pass only one argument')
    inputJson = json.loads(sys.argv[1].replace('\'', '"')
                productsIDs=inputJson["productsIDs"]
                for p in productsIDs:
                        print(p)
                        price = subprocess.check_output(['python', 'getPriceOfProdFromDB.py', str(p)], shell=True)
                        totalPrice = totalPrice + int(price)
        print(totalPrice)
        outputJson['output'] = {'totalPrice':totalPrice}
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = 'ERROR: ' + str(err) + '.'
finally:
    print(json.dumps(outputJson))
