class Solution:
    def startStation(self, gas, cost):
        total_gas = 0
        total_cost = 0
        current_fuel = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_fuel += gas[i] - cost[i]
            
            if current_fuel < 0:
                start_station = i + 1
                current_fuel = 0
        
        if total_gas < total_cost:
            return -1
        
        return start_station
