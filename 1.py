#banana camel problem

total_bananas=int(input("No. of bananas"))
distance=int(input("Distance to be covered"))
load_capacity=int(input("Maximum bananas it can carry"))
bananas_lost=0;

start=total_bananas
for i in range(distance):
    while start>0:
        start=start-load_capacity
        if start==1:
            bananas_lost=bananas_lost-1
        bananas_lost=bananas_lost+2
    bananas_lost=bananas_lost-1
    start=total_bananas-bananas_lost
    if start==0:
        break
print("Total bananas delivered:",start)