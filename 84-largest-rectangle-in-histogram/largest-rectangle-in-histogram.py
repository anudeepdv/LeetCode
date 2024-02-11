class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def union(low,mid,high):
            l1 = mid
            l2 = mid+1
            maxArea=0
            minheight=heights[l1]
            while(l1>= low and l2<=high):
                minheight = min(minheight,heights[l1],heights[l2])
                area = minheight*(l2-l1+1)
                maxArea=max(area,maxArea)

                if l1>low and l2 <high:
                    if heights[l1-1]>heights[l2+1]:
                        l1=l1-1
                    else:
                        l2=l2+1
                elif l1==low:
                    l2=l2+1
                else:
                    l1=l1-1
            return maxArea

        
        def mergeSort(low,high):
            if low==high:
                return heights[high]
            
            mid = low+(high-low)//2

            area1 = mergeSort(low,mid)

            area2 = mergeSort(mid+1,high)

            return max(area1,area2,union(low,mid,high))
        
        return mergeSort(0,len(heights)-1)