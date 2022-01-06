class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if capacity < 0: return False
        
        # trips are given in random order i want to get the last km where passengers are dropped off
        trips.sort(key=lambda trip: trip[2])
        
        # i want to keep track of the flow of passengers at each km
        flows = [0] * (trips[-1][-1] + 1)
        
        for trip in trips:
            size, start, end = trip
            
            flows[start] -= size
            flows[end] += size
            # print(flows)

        # tracks the flow of passengers for the car, if at anytime capcity goes below 0, then we have not enough capacity
        for flow in flows:
            capacity += flow
            if capacity < 0:
                return False
            
        return True
            