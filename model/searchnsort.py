
class My_searchbox:
    def linear_search(self,si,source):
        for i in source:
            if si in i:
                return int(source.index(i))
        return False