# task 1
# raw_data=[2,'N/A',4.5,"Error",10]
# new_data=[n**2 if type(n)==int or type(n)==float else 0 for n in raw_data ]
# print(new_data)


# task 2
# probs=[0.88, 0.21, 0.49, 0.51, 0.05]
# new_probs=['Positive' if n>=0.5 else 'Negative' for n in probs]
# print(new_probs)


# task 3
# ages=[12,23,45,27,65,90,8]
# new_ages=['Minor' if age<=18 else  'Adult' if age>18 and age<=64 else 'Senior' for age in ages ]
# print(new_ages)


# task 4
# users=['@AI', '@Developer', '@admin', '@ML']
# new_users=[x.lower()[1:] for x in users if len(x)>3]
# print(new_users)


# task 5
# data = [10, 20, 30, 40, 50, 60]
# mean = 30
# new_data = [n-30 for n in data]
# print(new_data)


# task 6
# prices = [10.5, -2.0, 500, 1200, 0, 95.9]
# new_prices=[p for p in prices if p>0 and p<1000]
# print(new_prices)


# task 7
files = ["data.csv", "profile.jpg", "notes.txt", "cat.jpg"]
new_files = [{'filename':f, 'is_image':True} if f.endswith('.jpg') else {'filename':f, 'is_image':False} for f in files]
print(new_files)