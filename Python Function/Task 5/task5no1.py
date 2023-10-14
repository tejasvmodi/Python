dict1={
	'Student1':{
	 	'rollno':27,
	 	'name':'Tejasv Modi',
	 	'semester':1,
	 	'Course':'MSCIT',
	 	'percentage':90
	},
	'student2':{
	 	'rollno':18,
	 	'name':'Smit Joshi',
	 	'semester':1,
	 	'Course':'MSCIT',
	 	'percentage':80
	},
	'student3':{
	 	'rollno':2,
	 	'name':'Bhavesh Patel',
	 	'semester':4,
	 	'Course':'MCA',
	 	'percentage':67
	},
	'student4':{
	 	'rollno':34,
	 	'name':'Tanish Modi',
	 	'semester':4,
	 	'Course':'BSCIT',
	 	'percentage':90
	},
	'student5':{
	 	'rollno':12,
	 	'name':'Nirav Patel',
	 	'semester':3,
	 	'Course':'MCA',
	 	'percentage':85
	}
}

print(dict1)


dict1['student3']['semester']=2

print()
print(dict1)

del dict1['student4']
print()
print(dict1)

dict2=dict1.copy()
print()
print(dict2)

print()
print("length of 1st dictionary",len(dict1))
print("length of 2nd dictionary",len(dict2))