#   Dhruvin Patel
#   Project 1
#   BFS Word Chain

from collections import deque
import copy

class Word:
    word = ""
    path = []
    def __init__(self,word):
        self.word = word
        self.path = []

#reads in the words dictionaries
def readin_dict(fileName):
    words = {}
    print("Using file : "+fileName)
    file = open(fileName, "r")
    for word in file:
        words.update({word.rstrip():word.rstrip()})
    return words 
        
def findAdjacentWords(word,dictionary):
    adj = []
    a_Z = [chr(i) for i in range(ord('a'), ord('z')+1)]
    
    #finds adjacent words with length 3
    if(len(word) >= 3):
        for i in range(0,len(word)):
            newWord = word[:i] + word[i+1:]
            if newWord in dictionary:
                adj.append(newWord)
    
    #finds adjacent words with length 4
    for i in range(0,len(word)): 
        for x in range(0,len(a_Z)):
            newWord = word[:i] + a_Z[x] + word[i+1:]
            if newWord in dictionary and newWord != word:
                adj.append(newWord)
                
    #finds adjacent words with length 5           
    if(len(word) <= 5):
        for i in range(0,len(word)): 
            for x in range(0,len(a_Z)):
                newWord = word[:i] + a_Z[x] + word[i:]
                if newWord in dictionary and newWord != word:
                    adj.append(newWord)
    
    #returns a list fo adj words
    return adj

def traverse(startWord, endWord, words):
    visited = set()
    queue = deque()
    
    #start the queue with the starting word and set counter
    start = Word(startWord)
    queue.append(start)
    counter = 0
    
    while queue:
        #dequeue the first nodes and check for equal endword
        s = queue.popleft()
        if endWord == s.word:
            print(str(counter-1) + " levels")
            print(str(len(visited)) + " nodes vistied")
            s.path.append(s.word)
            return s
        else:
            #add the word to the visited nodes list
            visited.add(s.word)
            
            #pop off the next nodes and copy the queue
            lvl = deque()
            lvl = copy.copy(queue)
            
            #find adjacent words for the node and all it to the queue
            adj = findAdjacentWords(s.word,words)
            for i in adj:
                if(i in visited):
                    continue
                else:
                    x = Word(i)
                    x.path.extend(s.path)
                    x.path.append(s.word)
                    queue.append(x)
            counter = counter + 1
            
            #while copy queue is not empty check all nodes at the level
            #if end word is found return the word with the path
            while(lvl):
                s = lvl.popleft()
                visited.add(s.word)
                queue.popleft()
                
                if endWord == s.word:
                    print(str(counter-1) + " levels")
                    print(str(len(visited)) + " nodes visited")
                    s.path.append(s.word)
                    return s
                adj = findAdjacentWords(s.word,words)
                for i in adj:
                    if(i in visited):
                        continue
                    else:
                        x = Word(i)
                        x.path.extend(s.path)
                        x.path.append(s.word)
                        queue.append(x)

#reading in the dictionaries
words = readin_dict("three_lc.txt")
words.update(readin_dict("old_four.txt"))
words.update(readin_dict("five_lc.txt"))

#check starting and ending words and traverse to find word path
while True:
    print("\nEnter any 3, 4, or 5 length word for start and end")
    startWord = input("Enter starting word:\n").lower()
    if startWord in words:
        endWord = input("Enter ending word:\n").lower()
        if endWord in words:
            path = traverse(startWord, endWord, words)
            print(' -> '.join(path.path))
        else:
            print("Ending word not valid")
    else:
        print("Starting word not valid")
    if input("To repeat enter r or enter any other key to quit\n").lower() != 'r':
        break;
        
    
