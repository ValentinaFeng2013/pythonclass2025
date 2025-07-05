# hw assignment 1
list_input = [1,2,3,4,5,2,4,6,7,8,9,7,10,10]
list_output = []
for i in list_input:
    if (i % 2 == 0) & (i not in list_output):
        list_output.append(i)
print(list_output)

# hw assignment 2
import time
start_time = time.time()
for i in range(10):
    for j in range(10):
        for p in range(10):
            for q in range(10):
                ps=str(i) + str(j) + str(p) + str(q)
                if ps=="7856":
                    print("Access granted!")
                    print("""
                                 ___
                                |   |
                               _|_____
                              |       |
                              |   ?   |
                              |_______|
                                              """)

                    break
end_time = time.time()
used_time = end_time - start_time
print(f"You used {used_time} secs")
#
#

list_na =[0,1,2,3,4,5,6,7,8,9,
          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
         ]
start_time = time.time()
for i in list_na:
    for j in list_na:
        for p in list_na:
            for q in list_na:
                ps=str(i) + str(j) + str(p) + str(q)
                if ps=="78av":
                    print("Access granted!")
                    print("""
                                 ___
                                |   |
                               _|_____
                              |       |
                              |   ?   |
                              |_______|
                                              """)

                    break
end_time = time.time()
used_time = end_time - start_time
print(f"You used {used_time} secs")
