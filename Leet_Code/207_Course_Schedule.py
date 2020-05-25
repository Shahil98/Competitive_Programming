class Solution(object):
    def __init__(self):
        self.matrix = []
        self.inDegree = []
        self.n = 0
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        for i in range(numCourses):
            arr = []
            for j in range(numCourses):
                arr.append(0)
            self.matrix.append(arr)
        self.n = numCourses
        for i in range(numCourses):
            self.inDegree.append(0)
        for i in range(len(prerequisites)):
            self.matrix[prerequisites[i][0]][prerequisites[i][1]] = 1
            self.inDegree[prerequisites[i][1]] = self.inDegree[prerequisites[i][1]] + 1
        self.n = numCourses
        
        queue = []
        for i in range(self.n):
            if(self.inDegree[i]==0):
                queue.append(i)
        count = 0
        while(len(queue)!=0):
            node = queue.pop(0)
            count = count + 1
            for i in range(self.n):
                if(self.matrix[node][i]==1):
                    self.inDegree[i] -= 1
                    if(self.inDegree[i]==0):
                        queue.append(i)
        if(count == self.n):
            return(True)
        else:
            return(False)
                
                
            
        