import random
import math
from time import time

print("Type speed calculator!")
print("----------------------")

def typetest():
    print("Your randomated sentence is: ")
    print()
    
    list1 = "Sometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind","She wrote him a long letter but he didn't read it","He didn’t want to go to the dentist yet he went anyway","Lets all be unique together until we realise we are all the same","I would have gotten the promotion but my attendance wasn’t good enough"

    num1 = random.randrange(0, 4)

    sent = list1[num1]
    print(sent)

    print()

    words = (len(sent.split()))

    sent = sent.lower()
    correct = (sent.split())

    try:
        print("Timer Started! \nType below:")
        start = time()
        text1 = input()
        end = time()
        total = round(end - start, 2)
        text1 = text1.lower()
        tlist = text1.split()
        if len(tlist) != words:
            print()
            print("You didnt finish!")
        else:
            print("Your time was %s seconds" % total)
            total = int(total) / 60
            print("Speed was %s wpm" % (str(words // total)))
            endtotal = 0
            for nums in tlist:
                if nums == correct[tlist.index(nums)]:
                    endtotal += 1
            endtotal = endtotal / len(correct)
            endtotal = endtotal * 100
            endtotal = round(endtotal, 1)
            if endtotal == 100:
                print("Perfect! your accuracy was 100%!!!")
            else:
                print("Your accuracy while typing was: ", endtotal, "%", sep="")

     
    except KeyboardInterrupt:
        print("")
    return 1

def main():
    print()
    number1 = 0
    number1 = typetest()
    print("----------------------")
    print()
    if number1 == 1:
        print("To try again type 1")
        retry = (int(input()))
        if retry == 1:
            print("----------------------")
            main()
main()
    
