class Customer:
    def __init__(self,name):
        self._name = name 
        self._points = 0 
    
    def updatePoints(self, bill):
        newPoints = bill // 10 
        self._points += newPoints
    
    
    def displayPoints(self):
        print(self._points)
        
        

#cust1 = Customer("Alan") 
#print(cust1._name)
#bill = int(input("Please enter the bill: "))
#Customer.updatePoints(cust1,bill)
#print(cust1._points)
customers = [] 
for x in range(5):
    name = input("Enter the customer name: ") 
    c = Customer(name)
    customers.append(c)


for x in customers:
    amount = int(input("How much was the bill?: "))
    x.updatePoints(amount)

for j in customers: 
    print(j._name, "   ", "Points: ",j._points)
    


        