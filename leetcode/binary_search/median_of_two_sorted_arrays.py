def find_median_sorted_arrays( nums1: list[int], nums2: list[int]) -> float:
       if len(nums1) > len(nums2):
           return find_median_sorted_arrays(nums1=nums2, nums2=nums1)
       left = 0
       right = len(nums1)
       total = len(nums1) + len(nums2)
       particion = (total + 1) // 2

       while left <= right:
           mid_a = (left + right) // 2
           mid_b = particion - mid_a

           a_izq = nums1[mid_a - 1] if mid_a > 0 else float("-inf")
           a_der = nums1[mid_a] if mid_a < len(nums1) else float("inf")

           b_izq = nums2[mid_b - 1] if mid_b > 0 else float("-inf")
           b_der = nums2[mid_b] if mid_b < len(nums2) else float("inf")

           if a_izq > b_der:
                right = mid_a - 1
           elif b_izq > a_der:
                left = mid_a + 1
           else:
               if total % 2 == 0:
                   return (max(a_izq,b_izq) + min(b_der,a_der)) / 2
               return max(a_izq,b_izq)

print(find_median_sorted_arrays([1,3],[2]))
print(find_median_sorted_arrays([],[1]))