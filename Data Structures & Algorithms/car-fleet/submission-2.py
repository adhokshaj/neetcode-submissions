class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort()

        fleets = 0
        prev_time = float('inf')

        while pos_speed:
            # print(pos_speed, prev_time, fleets)
            if prev_time == float('inf') and pos_speed:
                top = pos_speed.pop()
                pos = top[0]
                vel = top[1]
                t = (target-pos)/vel
                prev_time = t
                fleets += 1
                continue
            
            top = pos_speed.pop()
            pos = top[0]
            vel = top[1]
            t = (target-pos)/vel

            if t <= prev_time:
                continue
            else:
                prev_time = t
                fleets += 1

        # print(pos_speed, prev_time, fleets)
        return fleets

            
