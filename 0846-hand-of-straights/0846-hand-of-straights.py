class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        for card in hand:
            curr = card
            # see the lowest we can go to
            while count[curr - 1]:
                curr -= 1
                
            while curr <= card:
                while count[curr]:
                    for next_card in range(curr, curr + groupSize):
                        if not count[next_card]:
                            return False
                        count[next_card] -= 1
                curr += 1
        return True