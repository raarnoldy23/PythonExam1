# for loop 


#basic for loop 
for num in range(1, 10,1):
    print(num)

# for loop with user input
count = int (input('How many time do you want to loop?'))
for num in range(1, count+1):
    print('The count is:', num )

# Running count 
add = int (input(' how many values do you want to add?')) 
sum =0 
for count in range(1,add):
    sum = sum + count 
    
print('The Final count is:', count) 

