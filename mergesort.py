import math

class MergeSorter:
    'Merge sorts...'

    def __merge(self, arr1, arr2):
        arr1Index = 0
        arr1Length = len(arr1)

        arr2Index = 0
        arr2Length = len(arr2)

        result = []

        smallerArrayLength = arr1Length if arr1Length < arr2Length else arr2Length

        while (arr1Index < smallerArrayLength and
               arr2Index < smallerArrayLength):
               
            if (arr1[arr1Index] < arr2[arr2Index]):
                result.append(arr1[arr1Index])
                arr1Index += 1
            else:
                result.append(arr2[arr2Index])
                arr2Index += 1

        while arr1Index < arr1Length:
            result.append(arr1[arr1Index])
            arr1Index += 1

        while arr2Index < arr2Length:
            result.append(arr2[arr2Index])
            arr2Index += 1

        return result


    def sort(self, array):
        if len(array) == 1:
            return array
        else:
            arrayLength = len(array)
            arrayHalf = int(math.floor(arrayLength/2))

            return self.__merge( self.sort(array[0:arrayHalf]),
                                 self.sort(array[arrayHalf:arrayLength]) )

a = MergeSorter()
print(a.sort([3, 2, 6, 2, 5, 1, 9]))
