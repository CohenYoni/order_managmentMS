import tkinter as tk
import os, subprocess, json, time, sqlite3

DBname = 'ordersManagmentDB.db'
pathToDB = os.getcwd() + '\\' + DBname
orderTableName = 'orders'
itemsOfOrdersTableName = 'itemsOfOrder'

def showErrorDetails(err):
    subprocess.Popen(['java', '-cp', 'java-json.jar;', 'ShowError', json.dumps({'error': str(err)})], shell=True)
    print('running at background...')

# override tkitner handling exceptoin function
def custom_report_callback_exception(self, exc_type, exc_value, exc_traceback):
    showErrorDetails(exc_value)
tk.Tk.report_callback_exception = custom_report_callback_exception

class MainPane():
    #static variables
    btnWidth = 40
    defaultFont = ("Courier", 15)
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Orders Management')
        headerLbl = tk.Label(self.root, text="Welcome to Orders Management app",fg="blue")
        headerLbl.config(font = MainPane.defaultFont)
        headerLbl.grid(row=0)
        createOrderBtn = tk.Button(self.root, text='Create New Order', width=MainPane.btnWidth, command=self.createNewOrder)
        createOrderBtn.config(font = MainPane.defaultFont)
        createOrderBtn.grid(row=1)
        showOrdersBtn = tk.Button(self.root, text='Show All Orders', width=MainPane.btnWidth, command=self.showAllOrders)
        showOrdersBtn.config(font = MainPane.defaultFont)
        showOrdersBtn.grid(row=2)
        showIncomsBtn = tk.Button(self.root, text='Show Incomes From Orders', width=MainPane.btnWidth, command=self.showIncomesFromOrders)
        showIncomsBtn.config(font = MainPane.defaultFont)
        showIncomsBtn.grid(row=3)
        showInventoryBtn = tk.Button(self.root, text='Show Inventory', width=MainPane.btnWidth, command=self.showInventory)
        showInventoryBtn.config(font = MainPane.defaultFont)
        showInventoryBtn.grid(row=4)

    def start(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()

    def createNewOrder(self):
        def addProducts():
            def addProductToOrder():
                prodID = prodEntry.get()
                if prodID != '' and prodID.isnumeric() and int(prodID) in allProductsIDs and int(prodID) not in productIDs:
                    productIDs.append(int(prodID))
                    prodEntry.delete(0, tk.END)
                elif int(prodID) in productIDs:
                    showErrorDetails('You already inserted the product!')
                else:
                    showErrorDetails('Wrong product ID!')
                    
            def finish():
                if len(productIDs) != 0:
                    date = time.strftime("%d/%m/%Y")
                    connectDB = sqlite3.connect(pathToDB)
                    cursorDB = connectDB.cursor()
                    record = cursorDB.execute('SELECT MAX(ordID) FROM {0};'.format(orderTableName))
                    lastOrdID = record.fetchone()[0]
                    cursorDB.execute('INSERT INTO {0} (ordID, custName, custPhone, ordDate) VALUES ({1}, "{2}", "{3}", "{4}");'.format(orderTableName, lastOrdID + 1, name, phone, date))
                    productsNames = []
                    for prodID in productIDs:
                        cursorDB.execute('INSERT INTO {0} (ordID, productID) VALUES ({1}, {2});'.format(itemsOfOrdersTableName, lastOrdID + 1, prodID))
                        jsonToGetNameMS = {'DBlocation':pathToDB , 'prodID':prodID}
                        nameJson = json.loads(subprocess.check_output(['python', 'getNameOfProductFromDB.py', json.dumps(jsonToGetNameMS)], shell=True))
                        productsNames.append(nameJson['output']['prodName'])
                    connectDB.commit()
                    order = {
                                'ordID':lastOrdID+1,
                                'custName': name,
                                'custPhone': phone,
                                'ordDate': date,
                                'productsIDs': productIDs
                            }
                    totalPriceJson = json.loads(subprocess.check_output(['python', 'MSsumTotalPrice.py', json.dumps({'DBlocation': pathToDB, 'order': order})], shell=True))
                    if totalPriceJson['hadError']:
                        showErrorDetails(totalPriceJson['error'])
                    prodLbl.destroy()
                    prodEntry.destroy()
                    addProdBtn.destroy()
                    finishBtn.destroy()
                    headerLbl = tk.Label(createOrderWindow, text="The order saved successfully!")
                    headerLbl.config(font = MainPane.defaultFont)
                    headerLbl.grid(row = 0)
                    priceLbl = tk.Label(createOrderWindow, text="The total price of the order is {0}".format(totalPriceJson['output']))
                    priceLbl.config(font = MainPane.defaultFont)
                    headerLbl.grid(row = 1)
                    order.pop('productsIDs', None)
                    order['productsNames'] = productsNames
                    subprocess.Popen(['java', '-cp', 'java-json.jar;', 'ShowOrdersDetailsInList', json.dumps({'orders': [order,]})], shell=True)
                else:
                    showErrorDetails('You must add at least one product!')
                

            name = nameEntry.get()
            phone = phoneEntry.get()
            if 0 < len(name) <= 20 and 0 < len(phone) <= 10 and phone.isnumeric():
                nameLbl.destroy()
                nameEntry.destroy()
                phoneLbl.destroy()
                phoneEntry.destroy()
                addOrderBtn.destroy()
                prodLbl = tk.Label(createOrderWindow, text="Enter the product ID here: ")
                prodLbl.config(font = MainPane.defaultFont)
                prodLbl.grid(row = 0)
                prodEntry = tk.Entry(createOrderWindow, width = 20)
                prodEntry.grid(row=0, column=1, columnspan=50)
                productIDs = []
                addProdBtn = tk.Button(createOrderWindow, text='add product', command=addProductToOrder)
                addProdBtn.config(font = MainPane.defaultFont)
                addProdBtn.grid(row = 1)
                finishBtn = tk.Button(createOrderWindow, text='finish', command=finish)
                finishBtn.config(font = MainPane.defaultFont)
                finishBtn.grid(row = 1, column = 1)
                allProductsJson = json.loads(subprocess.check_output(['python', 'getAllProductsFromDB.py', pathToDB], shell=True))
                if allProductsJson['hadError']:
                    showErrorDetails(allProductsJson['error'])
                allProductsIDs = tuple(map(lambda x: x['prodID'], allProductsJson['output']))
                subprocess.Popen(['java', '-cp', 'java-json.jar;', 'ShowAllProductsInTable', json.dumps({'products': allProductsJson['output']})],shell=True)
            elif name == '':
                showErrorDetails('Please enter a name!')
            elif len(name) > 20:
                showErrorDetails('20 character maximum in the name!')
            elif phone == '':
                showErrorDetails('Please enter a phone number!')
            elif len(phone) > 10:
                showErrorDetails('10 digits maximum in the phone!')
            elif not phone.isnumeric():
                showErrorDetails('The phone number must include only digits!')
            else:
                showErrorDetails('Please enter correct input!')
            
                
        createOrderWindow = tk.Tk()
        createOrderWindow.title('Create Order')
        nameLbl = tk.Label(createOrderWindow, text="Full Name: ")
        nameLbl.config(font = MainPane.defaultFont)
        nameLbl.grid(row = 1)
        nameEntry = tk.Entry(createOrderWindow, width = 25)
        nameEntry.config(font = MainPane.defaultFont)
        nameEntry.grid(row=1, column=1)
        phoneLbl = tk.Label(createOrderWindow, text="Phone number: ")
        phoneLbl.config(font = MainPane.defaultFont)
        phoneLbl.grid(row = 2)
        phoneEntry = tk.Entry(createOrderWindow, width = 25)
        phoneEntry.config(font = MainPane.defaultFont)
        phoneEntry.grid(row=2, column=1)
        addOrderBtn = tk.Button(createOrderWindow, text='create', command=addProducts)
        addOrderBtn.config(font = MainPane.defaultFont)
        addOrderBtn.grid(row=3)

    def showAllOrders(self):
        allOrdersJson = json.loads(subprocess.check_output(['python', 'getAllOrdersFromDB.py', pathToDB], shell=True))
        if allOrdersJson['hadError']:
            showErrorDetails(allOrdersJson['error'])
        for order in allOrdersJson['output']:
            productsNames = []
            for prodId in order['productsIDs']:
                jsonToGetNameMS = {'DBlocation':pathToDB , 'prodID':prodId}
                nameJson = json.loads(subprocess.check_output(['python', 'getNameOfProductFromDB.py', json.dumps(jsonToGetNameMS)], shell=True))
                productsNames.append(nameJson['output']['prodName'])
            order.pop('productsIDs', None) #remove the productIDs key from the dictionary
            order['productsNames'] = productsNames
        subprocess.Popen(['java', '-cp', 'java-json.jar;', 'ShowOrdersDetailsInTable', json.dumps({'orders': allOrdersJson['output']})],shell=True)
        print('running at background...')

    def showIncomesFromOrders(self):
        allOrdersJson = json.loads(subprocess.check_output(['python', 'getAllOrdersFromDB.py', pathToDB], shell=True))
        if allOrdersJson['hadError']:
            showErrorDetails(allOrdersJson['error'])
        totalIncomes = 0
        for order in allOrdersJson['output']:
            jsonToSumTotalPrice = json.dumps({'DBlocation': pathToDB, 'order': order})
            totalPriceOrderJson = json.loads(subprocess.check_output(['python', 'MSsumTotalPrice.py', jsonToSumTotalPrice], shell=True))
            if totalPriceOrderJson['hadError']:
                showErrorDetails(totalPriceOrderJson['error'])
            totalIncomes += totalPriceOrderJson['output']
        showIncomeWindow = tk.Tk()
        showIncomeWindow.title('Incomes')
        headerLbl = tk.Label(showIncomeWindow, text="The incomes from all the orders are", fg="green")
        headerLbl.config(font=MainPane.defaultFont)
        headerLbl.grid(row=0)
        incomeLbl = tk.Label(showIncomeWindow, text=str(totalIncomes) + '$')
        incomeLbl.config(font=MainPane.defaultFont)
        incomeLbl.grid(row=1)

    def showInventory(self):
        allProductsJson = json.loads(subprocess.check_output(['python', 'getAllProductsFromDB.py', pathToDB], shell=True))
        if allProductsJson['hadError']:
            showErrorDetails(allProductsJson['error'])
        subprocess.Popen(['java', '-cp', 'java-json.jar;', 'ShowAllProductsInList', json.dumps({'products': allProductsJson['output']})], shell=True)
        print('running at background...')
        

try:
    main = MainPane()
    main.start()
    exit(0) #after mainloop finished
except Exception as err1:
    try:
        showErrorDetails(err1)
        main.close()
    except Exception as err2: #if showErrorDetails also raise exception
        print(err2)

