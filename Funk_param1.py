def her():
    
    a = b = 0
    
    while (a and b) != 100:
        a = int(input())
        b = int(input())

        if(a == b):
            break
        else:
            if a < b:
                print(f'{a} < {b}')
            else:
                print(f'{a} > {b}')
    print(f'OK {a} == {b}')            
        
her()