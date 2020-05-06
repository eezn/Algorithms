import random

def testing_random():
    """ random module test """
    values = [1, 2, 3, 4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    """ shuffle values list """
    random.shuffle(values)
    print(values)

    """ 0~10의 임의의 정수를 생성한다."""
    print(random.randint(0, 10))
    print(random.randint(0, 10))

if __name__=="__main__":
    testing_random()