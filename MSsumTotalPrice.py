import sys
import json
if len(sys.argv) == 2:
        try:
                string=sys.argv[1].replace("\'", "\"")

                print(string)
                order = json.loads(string)
                print(order)

        except ValueError:
                print ("That was invalid argument.  Try again...")
                exit(1)
        names=order["name"]
        print(names)
        for n in names:
                print(n)
                #price = usingMicroService(n)
                #totalPrice = totalPrice + int(price)
        #print(totalPrice)
        #exit(0)
        else:
                print('Error Argument')
                sys.exit(1)
