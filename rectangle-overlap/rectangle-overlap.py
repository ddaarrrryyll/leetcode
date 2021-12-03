class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1
        x3,y3,x4,y4 = rec2
        
        # if both rectangles overlap, a rectangle will be formed
        # bot left x, y
        bl_x = max(x1, x3)
        bl_y = max(y1, y3)
        
        # top right x, y
        tr_x = min(x2, x4)
        tr_y = min(y2, y4)
        
        if tr_x > bl_x and tr_y > bl_y:
            if (tr_x - bl_x) * (tr_y - bl_y) > 0:
                return True
        
        return False