names=[]

for x in range(0,10):
    n1=input("enter name: ")
    names.append(n1)
keepsearching = True
while keepsearching:
    Search = input('Search for names or type "End" to stop: ')
    if Search in names:
        print("name found")
    elif Search =="End":
        keepsearching=False
        continue
    else:
        print("name not found")
    
        
    
        
        
    
        
