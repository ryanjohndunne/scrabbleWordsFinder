"""
This program Displays:
1. Largest Group of Anagrams.
2. Scrabble word finder using query string.
3. Scrabble word finder with wildcard query string.
"""


class wordAndSorted(object):
    def __init__(self, originalWord=None, signature=None):
        self.originalWord = originalWord
        self.signature = signature


# Task One
def countingSort(word, maxLength):
    """
    Takes a word and sorts it alphabetically:
    Time complexity: O(n)  / O(N+D) but alphabet is a constant value of 27
    Space complexity: O(n) / O(N+D) but alphabet is a constant value of 27
    """

    # Save the unaltered word:
    currentWord = wordAndSorted()
    currentWord.originalWord = word

    # Output list which has sorted word
    output = [0 for i in range(27)]

    # Count array that contains count of individual letters
    count = [0 for i in range(27)]

    # String to contain sorted word
    signature = []

    # Count occurences of letter
    for i in word:
        count[ord(i.upper()) - 65] += 1

    # Build output list
    for i in range(27):
        while count[i] > 0:
            output[i] = chr(i + 65)
            signature.append(output[i])
            count[i] -= 1

    # Fill the rest of the word with null's so we can compare longer words
    for i in range(maxLength - len(signature)):
        signature.append('')

    # Store the sorted word into the word object
    currentWord.signature = signature

    return currentWord


def radixSort(sortedList, index, alphabet):
    """
    Takes a list of words and sorts them all alphabetically
    Time complexity: O(MN)  / O((N+D)M) but D is constant in alphabet at 27
    Space complexity: O(MN) / O((N+D)M) but D is constant in alphabet at 27
    """
    # For each word
    # Sort at the current index alphabetically
    for word in sortedList:
        if word.signature[index] != "":
            alphabet[ord(word.signature[index].upper()) - 64].append(word)
        else:
            # When blank space is detected place it at 0
            alphabet[0].append(word)
            pass

    # Store back into list
    sortedList[:] = []
    for letter in alphabet:
        sortedList.extend(letter)


def searchLargestAnagram(sortedList):
    """
    Sorts through the sortedList and finds all matching anagrams
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    currentAnagram = []
    largestAnagram = []
    maxCount = 0
    currentCount = 0
    nextWord = ""

    # Seach every word in list - 2
    for i in range(len(sortedList) - 2):
        nextWord = sortedList[i + 1]
        currentAnagram.append(sortedList[i])
        # If current word is the same as the next one, anagram match found
        if sortedList[i].signature == nextWord.signature:
            currentCount += 1
            if currentCount > maxCount:
                maxCount = currentCount
                largestAnagram = currentAnagram
        # If it's not a match, reset the values
        else:
            currentAnagram = []
            currentCount = 0

    print("The largest group of anagrams:", end=' ')
    for word in largestAnagram:
        print(word.originalWord, end=' ')


def largestAnagram(wordList, maxLength):
    """
    Takes a list of words and the maximum word length
    Returns the largest occuring anagram
    Time Complexity: O(MN)
    Space Complexity: O(MN)
    """
    sortedList = []

    # Sort every word into their unique signature
    # that is them sorted alphabetically
    for word in wordList:
        currentWord = countingSort(word, maxLength)
        # Append original + sorted word to list
        sortedList.append(currentWord)

    # For each column in the list, radix sort it
    # Starts at least significant digit
    for i in range(maxLength - 1, -1, -1):
        alphabet = [[] for _ in range(27)]
        radixSort(sortedList, i, alphabet)

    # Find the most occuring anagram and print it
    searchLargestAnagram(sortedList)

    # Returns a list of all words sorted by their signature
    return(sortedList)


def readInDictionary(Dictionary, wordList):
    maxLength = 0
    # Open dictionary and read in all words to the wordList
    # Check length of each word to get the longest word's length
    with open(Dictionary) as f:
        for line in f:
            wordList.append(line.rstrip())
            if len(line) > maxLength:
                maxLength = len(line)

    return maxLength
# End of Task One


# Task Two
def binarySearch(sortedList, queryWord, maxLength):
    """
    Search through list for alphabetic signature that's == queryWord
    using binary search
    Then check positions behind and infront for matching queryWords
    to also be displayed
    Time Complexity: O(klogN + W)
    Binary search is O(klogN), W is the output size
    """
    first = 0
    last = len(sortedList) - 1
    found = False
    anagramList = []

    while first <= last and not found:
        midpoint = (first + last) // 2
        if sortedList[midpoint].signature == queryWord:
            found = True
            # append the word to the list and set it as the word we want
            anagramList.append(sortedList[midpoint])
        else:
            if "".join(queryWord) < "".join(sortedList[midpoint].signature):
                last = midpoint - 1
            else:
                first = midpoint + 1

    position = midpoint - 1  # Check left of midpoint
    midpoint = midpoint + 1  # Check right of midpoint

    # Get all equal words to the left and including mid point
    try:
        while sortedList[position].signature == queryWord:
            anagramList.append(sortedList[position])
            position -= 1
    except IndexError:
        pass

    # Check if the current position is still equal to the query
    try:
        if sortedList[position].signature == queryWord:
            anagramList.append(sortedList[position])
    except IndexError:
        pass

    # Get all equal words to the right of mid point
    try:
        while sortedList[midpoint].signature == queryWord:
            anagramList.append(sortedList[midpoint])
            midpoint += 1
    except IndexError:
        pass

    # Check if the current position is still equal to the query
    try:
        if sortedList[midpoint].signature == queryWord:
            anagramList.append(sortedList[midpoint])
    except IndexError:
        pass

    return anagramList


def getScrabbleWords(wordList, queryWord, maxLength):
    # Sort the word using counting sort
    sortedWord = wordAndSorted()
    sortedWord = countingSort(queryWord, maxLength)

    # Use binary search to find all words with that anagram
    anagramList = binarySearch(wordList, sortedWord.signature, maxLength)

    print("\nWords without using a wildcard:", end=" ")
    for word in anagramList:
        print(word.originalWord, end=" ")
# End of Task Two


# Task Three
def getWildCardWords(wordList, queryWord, maxLength):
    resetQuery = queryWord
    anagramList = []

    # For each letter in the alphabet
    for i in range(26):
        queryWord += chr(i + 65)

        sortedWord = wordAndSorted()
        sortedWord = countingSort(queryWord, maxLength)

        # Use binary search to find all words with that anagram
        anagramList.extend(binarySearch(wordList,
                           sortedWord.signature, maxLength))

        queryWord = resetQuery

    print("\nWords using a wildcard:", end=" ")
    for word in anagramList:
        print(word.originalWord, end=" ")
# End of Task Three


def main():
    wordList = []

    # Read in the dictionary storing it in wordList
    maxLength = readInDictionary("Dictionary.txt", wordList)

    # Find the anagram with the largest amount of words
    wordList = largestAnagram(wordList, maxLength)

    # Loop through user input to get all words that can be made for task 2 & 3
    queryWord = input("\nEnter the query string: ")
    while queryWord != "***":
        # All words with given query
        getScrabbleWords(wordList, queryWord, maxLength)

        # All word with given query + wildcard
        getWildCardWords(wordList, queryWord, maxLength)

        queryWord = input("\n\nEnter the query string: ")


main()
