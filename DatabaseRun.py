from firebase import firebase
import threading
import time
import random 

def Database_Post():
	threading.Timer(5.0, Database_Post).start()
	perc = random.uniform(50.2, 75.5)
	pH = random.uniform(6.1,8.3)
	Temp = random.uniform(10.8,24.2)
	CL001 = random.uniform(1.1,2.6)
	CL002 = random.uniform(0.75,0.98)
	data = {
			'Percentage': perc,
			'pH':pH,
			'Temp':Temp,
			'CL001':CL001,
			'CL002':CL002
			}

	result = firebase.put('/data-793f6-default-rtdb/Data Points/','Percentage',perc) #update data
	result = firebase.put('/data-793f6-default-rtdb/Data Points/','pH',pH) #update data
	result = firebase.put('/data-793f6-default-rtdb/Data Points/','Temp',Temp) #update data
	result = firebase.put('/data-793f6-default-rtdb/Data Points/','CL001',CL001) #update data
	result = firebase.put('/data-793f6-default-rtdb/Data Points/','CL002',CL002) #update data
def Get_Database():
	threading.Timer(10.0,Get_Database).start()
	PercResult = firebase.get('/data-793f6-default-rtdb/Data Points/Percentage','') #get data 
	pHResult = firebase.get('/data-793f6-default-rtdb/Data Points/pH','') #get data 
	TempResult = firebase.get('/data-793f6-default-rtdb/Data Points/Temp','') #get data 
	CL001Result = firebase.get('/data-793f6-default-rtdb/Data Points/CL001','') #get data 
	CL002Result = firebase.get('/data-793f6-default-rtdb/Data Points/CL002','') #get data 
	print('----------------------------------------------------------------')
	print(PercResult,pHResult,TempResult,CL001Result,CL002Result)
	print('----------------------------------------------------------------')


firebase = firebase.FirebaseApplication('https://------------rtdb.firebaseio.com/',None)
data = {
			'Percentage': perc,
			'pH':pH,
			'Temp':Temp,
			'CL001':CL001,
			'CL002':CL002
			}
result = firebase.post('/----------------rtdb/Tester1',data) #post data 




Database_Post() 
Get_Database()





#result = firebase.post('/data-793f6-default-rtdb/Tester1',data) #post data 
#result = firebase.get('/data-793f6-default-rtdb/Tester1','') #get data 
#result = firebase.put('/data-793f6-default-rtdb/Tester1/-MQ1gqJEuIF4Ki9G8EWb','Percentage',perc) #update data


