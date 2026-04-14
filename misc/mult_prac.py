import random
import time

ref_num = int(input("Reference Number: "))

counter = 0
time.time()

while counter < 10:
    mult_1 = 0
    if random.random() > 0.5:
        mult_1 = 1
    else:
        mult_1 = -1
    mult_2 = 0
    if random.random() > 0.5:
        mult_2 = 1
    else:
        mult_2 = -1
    
    num_1 = ref_num + mult_1 * random.randint(1, 10)
    num_2 = ref_num + mult_2 * random.randint(1, 10)

    ans = int(input(f'{num_1} x {num_2} = '))
    if ans == num_1 * num_2:
        counter += 1
        print("Correct")
    else:
        counter -= 1
        print("Wrong")

print(time.time())