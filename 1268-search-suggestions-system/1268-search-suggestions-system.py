class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left, right = 0, len(products)-1
        results = [[] for _ in range(len(searchWord))]
        
        for i in range(len(searchWord)):
            if left > right:
                break
            while left <= right and (len(products[left]) <= i or products[left][i] != searchWord[i]):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != searchWord[i]):
                right -= 1
            
            print(left, right)
            for k in range(left, min(left + 3, right + 1)):
                results[i].append(products[k])
        return results