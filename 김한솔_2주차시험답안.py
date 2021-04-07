#김한솔_2주차시험답안.py

print("=====1=====")
# 1. 파이썬에서 클래스를 작성하면서 은행계정을 간단하게 구현한 
# BankAccount클래스를 개발하고 있습니다. 
# 내부에 멤버 변수인 id, name, balance를 외부에서는 접근하기 
# 힘들게 이름 규칙을 사용해서 파이썬의 이름변경을 사용하려고 합니다. 
# 아래의 코드를 올바르게 수정해서 제출하세요. 



#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

print(account1._BankAccount__balance)



print("=====2=====")
# 2. 파이썬에서 개발자(Developer)클래스를 정의하려고 합니다. 
# 내부 멤버변수는 id, name이 저장되고 getSalary()라는 메서드를 
# 구현하려고 합니다. 근무한 날짜(일수)를 정수형식 
# 매개변수로 입력받아서 월급(하루 일당은 10만원)을 콘솔(화면)에 
# 출력하는 메서드로 구현해야 합니다. Developer클래스의 생성자를 통해 인스턴스를 초기화하고 
# getSalary()를 통해 월급을 출력하는 코드까지 완성해서 제출하세요. 
class Developer:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def getSalary(self, day):
        result = day * 100000
        print("월급: ", result)

dev = Developer(123, "홍길동")
dev.getSalary(20)


print("=====3=====")
# 3. 2번에서 구현한 Developer클래스를 상속받아서 
# WebDeveloper클래스를 구현하려고 합니다. 
# getSalary()를 상속받아서 재정의(덮어쓰기)를 통해 
# 월급(하루 일당은 20만원)으로 재정의한 코드로 구현해서 제출하세요. 
# Developer클래스와 WebDeveloper클래스의 인스턴스를 
# 각각 생성해서 결과를 출력해야 합니다. 

class WebDeveloper(Developer):
    def __init__(self,id,name,skill):
        Developer.__init__(self,id,name)
        self.skill = skill
    def getSalary(self,day):
        result = day * 200000
        print("웹 개발자 월급:", result)

webDev = WebDeveloper(456, "김한솔", "ios")
webDev.getSalary(20)


# 4. 파이썬에서 함수, 클래스, 모듈, 패키지에 대한 개념과 차이점을 
# 정리해서 제출하세요.

# 함수: 특정 작업을 수행하는 명령어의 모음으로, 이해하기 쉽고 재사용이 가능하고
#       유지보수가 쉬움
# 클래스: 사번,이름,부서코드 등의 데이터가 필요하고 입사,퇴사 같은 액션이 필요하다.
# 모듈: 함수나 변수 또는 클래스를 모아 놓은 파일 
# 패키지:도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리


print("=====5=====")
# 5. 파이썬의 정규표현식을 사용해서 어떤 문자열에 우편번호가 포함되어 
# 있다면 re모듈의 어떤 함수를 사용해서 손쉽게 검색(가져올 수 있는)하는 
# 코드를 작성하세요. 
# 매칭오브젝트를 리턴(bool(수식을 작성) True, False)
import re

bool(re.match('[0-9]'))
#/d{5}
# bool(re.search("\d{5}", "우리 동네 우편번호 53000"))
# >> True

# bool(re.match("\d{5}","우리 동네 우편번호 53000"))
# >> False



# s = "Apple is big company and apple is delicious"
# c = re.compile("apple")
# c.findall(s)
# >> 'apple'

# c = re.compile("apple", re. l)
# c. findall(s)
# >> ['Apple', 'apple']

# s = """Gee Gee Gee
# 너무 부끄러워
#
# 쳐다 볼 수 없어"""
# c = re.compile("^.+")       # ^시작 .글자하나 
# c.findall(s)                #
# >> ['Gee Gee Gee']
# c = re.compile("^.+", re.M)
# c.findall(s)
# >> ['Gee Gee Gee', '너무 부끄러워', '쳐다 볼 수 없어']