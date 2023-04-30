# Mark Bulmer - CIS 115 - 7-16-2021
# Most Frequent Character

# Finds most frequent character in a string.

def main():
    #creates a array with 26 values
    count = [0] * 26
    #alaphabet to check off of
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    frequent = 0

    #user enters a string to check
    userString = input('Enter a string:')

    #for loop that runs until there is no more characters
    for ch in userString:
        #changes the character to Uppper Case to check against our list of characters
        ch = ch.upper()

        #determines which letter it is
        index = letters.find(ch)

        #makes sure the index is at 0 or above
        if index >= 0:
            #adds 1 to the counting array for the letter
            count[index] = count[index]+1

    #goes through the array
    for i in range(len(count)):
        #checks to see which is higher
        if count[i] > count[frequent]:
            #assigns new value to frequent if its higher
            frequent = i

    #prints out the letter with the most frequency
    print('The character that appears most frequently in the' \
          ' string is ', letters[frequent], '.',sep='')

main()
