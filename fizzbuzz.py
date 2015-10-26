my_input = raw_input("Press 'Enter' to start the fizzbuzz!")
print my_input

for n in xrange(1, 101):
    if n % 15 == 0:
        print "FizzBuzz"
    elif n % 3 == 0:
        print "Fizz"
    elif n % 5 == 0:
        print "Buzz"
    else:
        print n
