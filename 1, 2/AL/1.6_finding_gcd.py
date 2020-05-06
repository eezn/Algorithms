# greatest common divisor, least common multiple
# 유클리드 호제법(Euclidean algorithm)

def finding_gcd(a, b):
    while(b != 0):
        result = b
        a ,b = b, a % b # 유클리드 호제법(Euclidean algorithm)
    return result

def finding_lcm(a, b):    
    return (a * b) // finding_gcd(a, b)
    
def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print(finding_lcm(number1, number2))
    print("pass")

if __name__=="__main__":
    test_finding_gcd()