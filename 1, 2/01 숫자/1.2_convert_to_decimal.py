# 진법을 변환하는 함수
# -> 10진법 (2 <= base <= 10)

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

def test_convert_to_decimal():
    number, base = 1, 2
    # number, base = 123, 8
    assert(convert_to_decimal(number, base) == 9) # 83
    print("테스트 통과!")

if __name__=="__main__":
    test_convert_to_decimal()