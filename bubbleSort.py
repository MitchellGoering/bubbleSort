#the bubble sort algorith takes an array as input and sorts it by repeatedly comparing neighboring values down the list, often many times, until no values need to be swapped.

sortme = [40, 22, 1, 80, 45, 34, 53, 67, 82, 243, 44, 31, 66, 4081, 17]     #the array we will sort into numerical order

def bubbleSort(sortme):                                                     #define the sorting algorith named bubbleSort
    switch = True                                                           #set the boolean value "switch" as a flag for whether to continue with sorting loop. setting at true ensures it runs at least once

    while(switch):                                                          #this while loop will run until switch = false, which won't happen if the if statement on line 11 is not run
        switch = False                                                      #switch = false sets the boolean switch to false, which will close the while loop unless it is set to true again
        for i in range(len(sortme) - 1):                                    #this introduces variable i, which is set to a sequence of numbers the length of our input array minus one
            if sortme[i] > sortme[i+1]:                                     #if a given position in the array is greater than the position after it...

                sortme[i], sortme[i+1] = sortme[i+1], sortme[i]             #...we set the variables to themselves swapped, such as 4, 3 = 3, 4 to swap the values in the array
                switch = True                                               #we set the switch boolean flag to true so that the while loop runs again

bubbleSort(sortme)                                                          #run the bubbleSort function
print(sortme)                                                               #print the list after bubbleSort function was called on it

# the time complexity of the bubblesort is at best O(n) and at worst O(n*n)
