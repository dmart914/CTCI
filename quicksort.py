import math

class QuickSorter:

    def __swap(self, array, indexOne, indexTwo):
        temp = array[indexOne]
        array[indexOne] = array[indexTwo]
        array[indexTwo] = temp
        return

    def __partition(self, array, start, end):
        pivotIndex = int(math.floor(((end-start)/2)))
        pivot = array[pivotIndex]
        rightOfWall = start+1

        # swap the pivot with the leftmost item
        self.__swap(array, start, pivotIndex)

        for i in range(rightOfWall, end+1):
            # if item lt pivot, swap and move wall up
            if array[i] < pivot:
                self.__swap(array, rightOfWall, i)
                rightOfWall += 1

        # finally, swap back pivot
        self.__swap(array, 0, rightOfWall-1)

        # return the new pivot index
        return rightOfWall-1


    def sort(self, array, start, end):
        if start < end:
            print(array)
            # Pick a pivot
            newPivotIndex = self.__partition(array, start, end)
            self.sort(array, start, newPivotIndex-1)
            self.sort(array, newPivotIndex, end)

            return array

        # Partition: reorder the array to elements with val less than the pivot
        # come before the pivot, and elements with val gt pivot come after
        # for i in range(0, len(array)):
        #     if array[i] > pivot:



a = [3, 4, 2, 1, 5, 8, 2, 5, 7, 7]
b = [3, 1]

c = QuickSorter()
print(c.sort(a, 0, len(a)-1))

# def swap(array, indexOne, indexTwo):
#     temp = array[indexOne]
#     array[indexOne] = array[indexTwo]
#     array[indexTwo] = temp
#     return
#
# def partition(array, start, length):
#     pivotIndex = int(math.floor(((length-1)-start)/2))
#     print(pivotIndex)
#     pivot = array[pivotIndex]
#     rightOfWall = start+1
#
#     # swap the pivot with the leftmost item
#     print(array)
#     swap(array, start, pivotIndex)
#     print(array)
#
#     for i in range(rightOfWall, length):
#         # if item lt pivot, swap and move wall up
#         if array[i] < pivot:
#             swap(array, rightOfWall, i)
#             rightOfWall += 1
#         print(array)
#
#     # finally, swap back
#     swap(array, 0, rightOfWall-1)
#
#     # return the new pivot index
#     print(array)
#     return rightOfWall-1
#
#
#
#
#
# print(partition(b, 0, len(b)))
