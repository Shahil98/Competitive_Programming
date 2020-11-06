class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary_neighbours = {}
        dictionary_patterns = {}
        if(beginWord not in wordList):
            for i in range(0,len(beginWord)):
                pattern = beginWord[:i] + "*" + beginWord[i+1:]
                
                if pattern in dictionary_patterns:
                    dictionary_patterns.append(beginWord)
                else:
                    dictionary_patterns[pattern] = [beginWord]
                
                if beginWord in dictionary_neighbours:
                    dictionary_neighbours[beginWord].append(pattern)
                else:
                    dictionary_neighbours[beginWord] = [pattern]
        
        for word in wordList:
            for i in range(0,len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                
                if pattern in dictionary_patterns:
                    dictionary_patterns[pattern].append(word)
                else:
                    dictionary_patterns[pattern] = [word]
                
                if word in dictionary_neighbours:
                    dictionary_neighbours[word].append(pattern)
                else:
                    dictionary_neighbours[word] = [pattern]
        print(dictionary_patterns)
        beginQueue = [(beginWord,1)]
        endQueue = [(endWord,1)]
        
        visitedBeginQueue = {}
        visitedEndQueue = {}
        
        visitedBeginQueue[beginWord] = 1 
        visitedEndQueue[endWord] = 1 
        
        if(endWord not in dictionary_neighbours):
            return(0)
        
        for patterns in dictionary_neighbours[beginWord]:
            if endWord in dictionary_patterns[patterns]:
                return(2)
        
        while beginQueue and endQueue:
            word1 = beginQueue.pop(0)
            word2 = endQueue.pop(0)
            
            
            if word1[0] in visitedEndQueue:
                return(visitedBeginQueue[word1[0]] + visitedEndQueue[word1[0]] - 1)
            elif word2[0] in visitedBeginQueue:
                return(visitedBeginQueue[word2[0]] + visitedEndQueue[word2[0]] - 1)
            
            for pattern in dictionary_neighbours[word1[0]]:
                for word in dictionary_patterns[pattern]: 
                    if word not in visitedBeginQueue:
                        beginQueue.append((word,word1[1]+1))
                        visitedBeginQueue[word] = word1[1]+1
                    
            for pattern in dictionary_neighbours[word2[0]]:
                for word in dictionary_patterns[pattern]:
                    if word not in visitedEndQueue:
                        endQueue.append((word,word2[1]+1))
                        visitedEndQueue[word] = word2[1]+1
        return(0)
            