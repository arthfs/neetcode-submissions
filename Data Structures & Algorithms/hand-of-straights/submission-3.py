from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        ref = Counter(hand)
        
        temp = []
        queue = sorted(list(ref.keys()))
     
        groups = []

        while queue!= [] :
            if temp == []:
                
                while queue!= [] and ref[queue[0]] == 0:
                    queue.pop(0)
                    
                if queue == []:
                    break
            
                temp.append(queue[0])
                ref[queue[0]] -=1

            if len(temp) == groupSize:
                groups.append(temp.copy())
                temp = []
                continue

            target = temp[-1] + 1
            if ref.get(target, 0) == 0 :
                return False
                    
            temp.append(target)
            ref[target] -=1
        
        return True