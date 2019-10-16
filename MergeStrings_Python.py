#PROGRAM DESCRIPTION: This program contains a function MergeStrings, which takes input of an array of strings #
#and returns a lowercase merged string sorted by character, clear of non-alphanumeric characters. #

# This function merges elements of an array into one string #
def MergeStrings(stringArray):
    finalString =""                                 # Buffer to hold string to return #
    joinedString = ''.join(stringArray)              # Merges the elements of the array into one string #
    for x in joinedString:                          # Loop through characters in the merged string #
        if x.isalpha():                             # Check if character is alphanumeric #
            finalString += x                        # If above condition is true, add character to string #

    buffer = sorted(finalString.lower())            # Sort the final string by character, but sorted() makes it an array #
    finalString = ''.join(buffer)                   # Merge the elements of buffer into one string #

    return finalString                              #Return corrrectly formatted merged string #


# This runs the function with a test array of strings and prints out the final merged string #
if __name__ == "__main__":
    testStrings = ["Rat", "dog", "cat", "shoe", "1"]
    mergedString = MergeStrings(testStrings)
    print(mergedString)