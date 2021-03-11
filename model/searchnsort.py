
class My_searching:
    def linear_search(self,si,source):
        for i in source:
            if si in i:
                return int(source.index(i))
        return False

class My_sorting:
    def insertion_sort(self,list_a,index):
        for i in range(1,len(list_a)):
            save = list_a[i]
            j=i
            while j>0 and list_a[j-1][index] > save[index]:
                list_a[j] = list_a[j-1]
                j -= 1
            list_a[j] = save
        return list_a



