items = []
def register(cost, payment):
	item = 0;
	if(cost == 1):
		item = items[0]
	elif(cost == 2):
		item = items[1]
	elif(cost == 3):
		item = items[2]
	elif(cost == 4):
		item = items[3]
	elif(cost == 5):
		item = items[4]
	return float("{0:.2f}".format(payment - item))
def change_machine(change):
	change = float("{0:.2f}".format(change))
	if(change <= 0.0):
		return
	elif(change >= 100000):
		bills = 0
		while(change >= 100000):
			bills+=1
			change-=100000
		print(str(bills), 'lembar 100.000')
		return change_machine(change)
	elif(change >= 50000):
		bills = 0
		while(change >= 50000):
			bills+=1
			change-=50000
		print(str(bills), 'lembar 50.000')
		return change_machine(change)
	elif(change >= 20000):
		bills = 0
		while(change >= 20000):
			bills+=1
			change-=20000
		print(str(bills), 'lembar 20.000')
		return change_machine(change)
	elif(change >= 10000):
		bills = 0
		while(change >= 10000):
			bills+=1
			change-=10000
		print(str(bills), 'lembar 10.000')
		return change_machine(change)
	elif(change >= 5000):
		coins = 0
		while(change >= 5000):
			coins+=1
			change-=5000
		print(str(coins), 'lembar 5.000')
		return change_machine(change)
	elif(change >= 2000):
		coins = 0
		while(change >= 2000):
			coins+=1
			change-=2000
		print(str(coins), 'lembar 2.000')
		return change_machine(change)
	elif(change >= 1000):
		coins = 0
		while(change >= 1000):
			coins+=1
			change-=1000
		print(str(coins), 'lembar 1.000')
		return change_machine(change)
	elif(change >= 500):
		coins = 0
		while(change >= 500):
			coins+=1
			change-=500
		print(str(coins), 'koin 500')
		return change_machine(change)
	elif (change >= 200):
		coins = 0
		while (change >= 200):
			coins += 1
			change -= 200
		print(str(coins), 'koin 200')
		return change_machine(change)
	elif (change >= 100):
		coins = 0
		while (change >= 100):
			coins += 1
			change -= 100
		print(str(coins), 'koin 100')
		return change_machine(change)
print('Total belanja seorang customer: ')
item_to_buy = items.append(int(input()))
print('Membeli barang dengan harga Rp.' + str(items[0]), 'Pembeli Membayar: ')
payment = float(input())
change = payment - items[0]
print('Your change is: Rp.' + str(change))
change_machine(change)