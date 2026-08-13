class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)

        prevTime=(target-pair[0][0])/pair[0][1]
        fleets=1

        for i in range(1,len(pair)):
            curr_car=pair[i]
            time=(target-curr_car[0])/curr_car[1]
            if time>prevTime:
                fleets+=1
                prevTime=time
        return fleets
