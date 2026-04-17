import random
import time

def memory_game():
    print("Xotira o‘yini boshlandi!")
    print("5 ta son chiqadi, ularni eslab qoling!")

    numbers = random.sample(range(1, 51), 5)
    print("Sonlar:", numbers)

    time.sleep(5) 

    print("\n" * 50)  

    user = []
    print("Endi eslagan sonlaringizni kiriting:")
    for i in range(5):
        son = int(input(f"{i+1}-son: "))
        user.append(son)

    togri = [x for x in user if x in numbers]

    print("Asl sonlar:", numbers)
    print("Siz topgan sonlar:", togri)
    print("Natija:", len(togri), "/ 5")

memory_game()
