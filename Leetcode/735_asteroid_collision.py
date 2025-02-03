class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #st = []
        i = 0
        while i < len(asteroids)-1: #O(n)
            #curr +ve and next is -ve
            if asteroids[i]>0 and asteroids[i+1] <0:
                #curr is larger than next
                if asteroids[i] > abs(asteroids[i+1]):
                    asteroids.pop(i+1)    #TC = O(n)
                    #The pop method has a time complexity of O(n) because it may need to shift elements in the list.
                #curr is smaller than next
                elif asteroids[i] < abs(asteroids[i+1]):
                    asteroids.pop(i)   ##TC = O(n)
                    if i>0:    #handled -ve
                        i -= 1
                #both are equal
                else:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    if i>0:  ##handled -ve
                        i -= 1
            else:
                i+=1
        return asteroids


#TC = O(n**2)
#SC = O(1)