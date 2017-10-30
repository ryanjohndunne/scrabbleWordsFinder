# scrabbleWordsFinder
Finds the longest group of anagrams in a given dictionary and returns all words from the dictionary that can be made with a given string. An additional "wildcard" letter is supported, returning all words that can be made with the query string + any letter a-z.

# How it works
# Finding the longest anagram.
## This takes O(MN) time and space complexity. Where M is the amount of words and N is the length of the words.
1. Read in each word from the dictionary - seperated by new lines
2. Sort each word into their alphabetic signature (this is the word sorted alphabetically) so leap becomes aelp. This sort is done using counting sort.
3. Using radix sort we sort the entire dictionary by their alphabetic signature so that all anagrams are listed next to each other.
4. Lastly, we go through the list looking for a matching anagram and counting how many there is. When a series of anagrams is detected we append it to a list. At the end of the dictionary the longest list is returned that contains an object wordAndSorted that contains the original word and the alphabetic signature.

# Finding each word of same length that can be made with a query string.
## This takes O(k log N + W) time complexity where W is the characters in the output size and k is the size of the word to sort.
1. Get the user input as query string and sort it using counter sort to get the alphabetic signature.
2. Using binary search we can search through the list for an equal string. if the string is equal to the query then we look to the left and right positions for all other signatures that are equal. Once they've all been found and appended to a list we can print each word out.

# Finding each word that can be made with query string + one additional letter which can be a-z.
## This takes O(k log N + W) where W is the characters in the output size and k is the size of the word to sort.
1. Add one letter from the alphabet each loop until the query string + 1 letter has fulfilled the entire alphabet  
2. Use Task two to search the list for matching anagrams

# How to run
have python 3 installed
python scrabble.py
enter the values you want to use as the query. 
Type "***" no quotations to exit the program.
