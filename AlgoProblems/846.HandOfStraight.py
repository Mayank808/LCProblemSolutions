from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # could optimize by using a heap instead of sort for invalid cases
        hand.sort()
        counts = Counter(hand)

        for card in hand:
            if not counts[card]:
                continue
            
            for x in range(card, card + groupSize):
                if x not in counts or counts[x] <= 0:
                    return False
                
                counts[x] -= 1
        
        return True
