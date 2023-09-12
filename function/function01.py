# def(define) -> 함수를 정의한다.

# 오버로딩 안됨!!!
def add(x, y):
    result = x + y
    return result



# 여러개의 매개변수, 여러개의 리턴은 튜플자료형으로 정의되어진다.
def add(*a):
    print(type(a))
    return list(a), 10

r = list(add(20, 10, 5, 30, 40))

print(r)

# **이면 딕셔너리 자료형으로 매개변수를 변환해준다.
def sub(**data):
    print(type(data))
    print(data)

sub(a=1, b=2)

def sub(data):
    print(type(data))
    print(data)

sub({"a": 1, "b": 2})

# 초기값이 없는 변수명은 앞쪽으로 줘야함.
def connection(serverName, password, ip="127.0.0.1", port="8080",  username="username"):
    print(f"ip: {ip}")
    print(f"prot: {port}")
    print(f"serverName: {serverName}")
    print(f"username: {username}")
    print(f"pasword: {password}")

# 변수명과 같이 적어준다.
connection(serverName="test_server", password="1q2w3e4r", port="3306")

a = 2

def multi(a):
    return a ** 2

a = multi(a)
print(a)

def div():
    global a
    a = a * 10

div()
print(a)

########################################################################

def add(a, b):
    return a + b

print(add(10, 20))

# 파이썬에서 람다는 하나의 명령만 수행할 수 있다.(여러줄 불가능)
add = lambda a, b: print(a + b)

add(30, 30)























