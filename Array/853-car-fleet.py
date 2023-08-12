# Not working 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

# At a point in time t, the cars would be at position + t*speed
# if before reaching the destination, they can match, then they become a fleet. 
        j = []
        if len(position)<2:
            return len(position)
        k = position 
        stack = {}
        counter = len(position)
        while(k):
            for i in range(len(k)):
                if stack:
                    if k[i] in stack:
                        counter -= 1 
                        stack[k[i]] = min(stack[k[i]], speed[i])
                        k.pop(i)
                        speed.pop(i)
                    else: 
                        stack[k[i]] = speed[i] 
                    k[i] += stack[k[i]]

                if k[i] == target:
                    k.pop(i)
        return counter 

            
## Issue: when we update the car positions, it still stores the old positions in the memory to compare, this needs to go, or we need 
# a different approach. 

''' In scenarios where the position is a continuous variable, and you're looking to determine when certain events 
(like fleet formation) occur, using time as the primary metric often simplifies the problem. 
Time becomes the common basis for comparison and allows you to make meaningful decisions 
based on the relative time of arrival at the destination.'''

# Hence, use time. 
## Logic - the cars taking smaller time will catch up at some point and form the fleet. 
# So, best to sort the time
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

# At a point in time t, the cars would be at position + t*speed
# if before reaching the destination, they can match, then they become a fleet. 
        car_data = sorted(zip(position,speed), reverse= True)

'''Calculating all times and then sorting them won't work correctly, 
as the order of the cars in the array has implications for fleet formation.'''
        fleets = 0
        time_to_reach = [(target - pos) / spd for pos, spd in car_data]
        max_time = 0

        for time in time_to_reach:
            if time > max_time:
                fleets += 1
                max_time = time
        
        return fleets

