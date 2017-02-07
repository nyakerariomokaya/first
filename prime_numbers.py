def is_prime():
    n = int(raw_input("Find the primes upto?:"))
    
    for num in range(0,n+1):
	is_prime = True
	for x in range(2,num):
	    if num % x  == 0:
	       is_prime = False
	       break
        if is_prime == True:
           print(num)
    
is_prime() 
