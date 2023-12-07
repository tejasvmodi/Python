dict1={
	'capital':{
		'spain':'Madrid',
		'france':'Paris',
		'germany':'Berlin',
		'norway':'Oslo'
	}
}

print(dict1['capital']['germany'])
del dict1['capital']['norway']
print()
print(dict1)

i1=input("Enter the country")
flag=0 
for i in dict1['capital']:
	if(i==i1):
		print(dict1['capital'][i])
		flag=1
		break 

if(flag==0):
	print("country is not present in dictionary")

dict1['capital']['india']='dehli'

print(dict1)