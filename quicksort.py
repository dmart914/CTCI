import math

class QuickSorter:

    def __swap(self, array, indexOne, indexTwo):
        temp = array[indexOne]
        array[indexOne] = array[indexTwo]
        array[indexTwo] = temp
        return

    def __partition(self, array, start, end):
        pivotIndex = int(math.floor(((end-start)/2)) + start)
        print('pivot index: ' + str(pivotIndex))
        pivot = array[pivotIndex]

        # swap the pivot with the leftmost item
        self.__swap(array, start, pivotIndex)
        rightOfWall = start+1

        for i in range(rightOfWall, end):
            # if item lt pivot, swap and move wall up
            if array[i] < pivot:
                print('swap! ' + str(rightOfWall) + ',' + str(i))
                self.__swap(array, rightOfWall, i)
                rightOfWall += 1
                print(str(array) + ', ROW: ' + str(rightOfWall))

        # finally, swap back pivot
        self.__swap(array, start, rightOfWall-1)

        # return the new pivot index
        print('returning ROW: ' + str(rightOfWall-1))
        return rightOfWall-1


    def sort(self, array, start, end):
        print('SORT: ' + str(array) + ',' + str(start) + ',' + str(end))
        if start < end:
            # Pick a pivot
            newPivotIndex = self.__partition(array, start, end)
            print('new pivot index: ' + str(newPivotIndex))
            self.sort(array, start, newPivotIndex-1)
            self.sort(array, newPivotIndex, end)

        return array



a = [3, 4, 2, 1, 5, 8, 2, 5, 7, 7]
b = [3, 1]

# c = QuickSorter()
# print(c.sort(a, 0, len(a)-1))

def swap(array, indexOne, indexTwo):
    temp = array[indexOne]
    array[indexOne] = array[indexTwo]
    array[indexTwo] = temp
    return

def partition(array, start, end):
    print('Partition start: ' + str(array))
    pivotIndex = int(math.floor(end-start) / 2) + start
    print('Pivot index: ' + str(pivotIndex))
    pivot = array[pivotIndex]
    print('Pivot value: ' + str(pivot))

    # swap leftmost element
    swap(array, start, pivotIndex)
    print(array)

    rightOfWall = start+1
    print('Right of wall index: ' + str(rightOfWall))

    for i in range(rightOfWall, end+1):
        if (array[i] < pivot):
            swap(array, i, rightOfWall)
            print('swap: ' + str(array) + ',' + str(i) + ',' + str(rightOfWall))
            rightOfWall += 1

    swap(array, start, rightOfWall-1)
    print('final swap: ' + str(array))
    print('returns pivot new pos: ' + str(rightOfWall-1))

    return (rightOfWall-1)



def sort(array, start, end):
    print('sort start: ' + str(start) + ',' + str(end))
    if start < end:
        newPartitionIndex = partition(array, start, end)
        sort(array, start, (newPartitionIndex - 1))
        sort(array, newPartitionIndex + 1, end)

    return array

print(sort(b, 0, len(b) - 1))

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
