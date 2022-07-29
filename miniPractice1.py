

def min_of(a):
    
    mini = a[0]
    for i in range(len(a)):
        if mini > a[i]:
            mini = a[i]
            
    return mini