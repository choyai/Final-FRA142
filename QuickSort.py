def quickSort(arr):
   helper(arr,0,len(arr)-1)

def helper(arr,first,last):
   if first<last:

       splitpoint = partition(arr,first,last)

       helper(arr,first,splitpoint-1)
       helper(arr,splitpoint+1,last)


def partition(arr,first,last):
   pivotvalue = arr[first]

   lwrLim = first+1
   upprLim = last

   done = False
   while not done:

       while lwrLim <= upprLim and arr[lwrLim] <= pivotvalue:
           lwrLim = lwrLim + 1

       while arr[upprLim] >= pivotvalue and upprLim >= lwrLim:
           upprLim = upprLim -1

       if upprLim < lwrLim:
           done = True
       else:
           temp = arr[lwrLim]
           arr[lwrLim] = arr[upprLim]
           arr[upprLim] = temp

   temp = arr[first]
   arr[first] = arr[upprLim]
   arr[upprLim] = temp


   return upprLim
