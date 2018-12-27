import sys
import json
import subprocess

outputJson = {'hadError':False, 'error':'', 'output':[]}
detailsJson={}
totalPrice = 0
try:
    if len(sys.argv) != 2:
        raise Exception('You need to pass only one argument')
    inputJson = json.loads(sys.argv[1].replace('\'', '"'))
    inputJson = inputJson['order']
    print(inputJson)                       
    detailsJson['DBlocation']=inputJson['DBlocation']
    productsIDs=inputJson['productsIDs']
                           
    for p in productsIDs:
        print(p)
        detailsJson['productsIDs'] = p
        outputFromGetPrice = subprocess.check_output(['python', 'getPriceOfProdFromDB.py', json.dumps(detailsJson)], shell=True)
        if(outputFromGetPrice["hadError"]==true)
            raise Exception(outputFromGetPrice["error"])
        JsonFromGetPrice=outFromGetPrice["output"]
        price=JsonFromGetPrice["price"]
        totalPrice = totalPrice + int(price)
        print(totalPrice)
        outputJson['output'] = {'totalPrice':totalPrice}
except Exception as err:
    outputJson['hadError'] = True
    outputJson['error'] = 'ERROR: ' + str(err) + '.'
finally:
    print(json.dumps(outputJson))


"{'DBlocation' : 'C:\Users\dell xps 9560\Desktop\microservices','order' : {'ordID' : '1234','custName' : 'May','custPhone' : '050……..','ordDate' : '24/8/2018','productsIDs' : [1, 2, 3]}}"
