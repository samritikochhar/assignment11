#Q 1
import re
mail=input('Type your Gmail ya yahoo ID only :')
count=0
matcher=re.finditer('[a-z A-z][a-z A-Z 0-9 _ .]*[@](gmail.com|yahoo.com)',mail)
for i in matcher:
    count+=1
    print('{} is a valid id'.format(i.group()))
if(count==0):
    print('Not valid')

#Q 2
import re
phn=(input('Enter the no.: +91-'))
count=0
matcher=re.finditer('^[6-9][0-9]{9}',phn)
for i in matcher:
    count+=1
    print('{} is a valid Indian no.'.format(i.group()))
if(count==0):
    print('Not valid')