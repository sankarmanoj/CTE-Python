def insertion(a):
        if len(a)==2:
            if a[0]>a[1]:
                a[0],a[1] = a[1],a[0]
                return a
            else:
                return a
