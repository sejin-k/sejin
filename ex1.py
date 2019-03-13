
# E x 1

# coding: utf-8

#####################################################################################
##############################  Basic python syntax  ################################
#####################################################################################


my_basket = ['clover', 'pansy', 'clover', 'rose', 'ivy', 'daisy']


# Q1. Show `my_basket` contents.
print('Ans1)', end = ' ')
print(my_basket)

# Q2. How many flowers in `my_basket`?
print('Ans2)', end = ' ')
print(len(my_basket))

# Q3. Are there any `pansy` in `my_basket`? <br/>
# (hint: use `in`)
print('Ans3)', end = ' ')

if 'pansy' in my_basket:
    print('yes')

# Q4. Are there any rose or daisy in `my_basket`? <br/>
#  (hint: use `or`, `in`)
print('Ans4)', end = ' ')

if 'rose' or ' daisy' in my_basket:
    print('yes, both are there')

# Q5. How many `clover` are in `my_basket`?
print('Ans5)', end = ' ')

n = 0
for i in range(len(my_basket)):
    if 'clover'== my_basket[i]:
        n = n+1

print('there are', end = ' ')
print(n, end = ' ')
print('clover')

# Q6. What kinds of flowers are in `my_basket`?
print('Ans6)', end = ' ')

kind = set(my_basket)
kind_ls = list(kind)
print(kind_ls)

# Q7. Put a `violet` into `my_basket` if it is not in the `my_basket`?
print('Ans7)', end = ' ')

if 'violet' not in my_basket:
    my_basket.append('violet')

print(my_basket)

# Q8. Show the name of flowers in `my_basket` ending with `y`.
print('Ans8)', end = ' ')

for i in range(len(my_basket)):
    if my_basket[i][-1] == 'y':
        print(my_basket[i], end = ' ')
print()


# Q9. Count the number for each kind of flowers in `my_basket`. (You may represent them as a dict name = `counter`)<br/>
#    ex) counter = {'clover': 2, 'daisy'  :1,  ..}
print('Ans9)', end = ' ')
counter = {}
for i in range(0, len(my_basket)):
    n = my_basket.count(my_basket[i])
    counter[my_basket[i]] = n

print(counter)

price = {'clover': 1500,
          'pansy': 1000,
          'rose': 2000,
          'ivy' : 500,
          'daisy' : 3000}

# Q10. update `violet` data at `price` dictionary. (`violet` price is 2500)
print('Ans10)', end = ' ')
price['violet'] = 2500
print(price)

# Q11. How much do I pay for flowers in `my_basket`.
print('Ans11)', end = ' ')
sum = 0
for i in range(len(my_basket)):
    sum += price[my_basket[i]] * counter[my_basket[i]]

print('flowers are : ', end = ' ')
print(sum)

# Q12. Add any flower in `my_basket` and update `price` dictionary. (flower name and price choose your own)
print('Ans12)', end = ' ')

my_basket.append('cosmos')
price[my_basket[-1]] = 4500

print(my_basket)
print(price)


#####################################################################################
##################################  Loop & Function  ################################
#####################################################################################

# ## 스스로 tester 작성하기: 예제
# 다음과 같이 test function이 주어져 있다:

# In[2]:

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# #### Q1. 절대값을 구하는 function `ablsolute_value`를 작성해서 다음과 같이 test해 보자.
# 모든 test case가 통과될 때 까지 code를 수정한다.

# In[3]:


def absolute_value(n):  # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        n *= -1
        return n
    elif n >= 0:
        return n


test(absolute_value(17) == 17)
test(absolute_value(-17) == 17)
test(absolute_value(0) == 0)
test(absolute_value(3.14) == 3.14)
test(absolute_value(-3.14) == 3.14)


# ## 다음 물음에 답하여 code를 작성하고, 함께 test case들도 작성한다.

# #### Q2. 정수를 매개 변수로 받아 각 자리를 제곱한 뒤 모두 더하는 `sum_of_digit_square` function을 작성하라.
# Parameter: 789 -> Output: 49+64+81=194

# In[4]:


def sum_of_digit_square(n):
    ans = 0
    n = absolute_value(n)
    change = str(n)
    for x in range(len(change)):
        ans += int(change[x])**2
    return ans

test(sum_of_digit_square(789) == 7 ** 2 + 8 ** 2 + 9 ** 2)
test(sum_of_digit_square(-123) == 1 ** 2 + 2 ** 2 + 3 ** 2)


# #### Q3. 2이상의 자연수를 매개 변수로 받아 소수인지 검사하는 `is_prime` function을 작성하라.

# In[5]:


def is_prime(n):
    for i in range(2, n+1):
        if n % i == 0 and n == i:
            return True
        elif n%i == 0 and n != i:
            return False
            break


test(is_prime(2) == True)
test(is_prime(5) == True)
test(is_prime(12) == False)
test(is_prime(13) == True)
test(is_prime(1033) == True)


# #### Q4. 2이상의 자연수를 인자로 받아, 아래와 같은 문양을 출력하는 `star_pattern` void function을 작성하라.

# input: 5일 떄, 다음을 출력
# ```python
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# ```

# In[6]:


def star_pattern(n):
    for i in range(1, n+1):
        print('*'*i)
    for i in range(n, 0, -1):
        print('*'*i)

star_pattern(5)
star_pattern(6)


# #### Q5. 자연수를 매개 변수로 받아 가장 가까운 완전 제곱수를 출력하는 `perfect_square` function을 작성하라.

# In[7]:


def perfect_square(n):
    ans = round(n**0.5)
    return ans


test(perfect_square(15) == 4)
test(perfect_square(31) == 6)
test(perfect_square(41) == 6)
test(perfect_square(99) == 10)


# #### Q6. 자연수를 매개 변수로 받아 각 자리의 수를 더하여 새로운 수를 구하고, 이를 반복하여 한 자리 수를 만들어 출력하는 `unit_place_value` function을 작성하라.
# (e.g., 75 -> 7+5=12 -> 1+2=3).

# In[8]:


def unit_place_value(n):
    while n >= 10:
        sum = 0
        num_str = str(n)
        for i in range(len(num_str)):
            sum += int(num_str[i])
        n = sum

    if n < 10:
        return n
    return sum


test(unit_place_value(75) == 3)
test(unit_place_value(3942) == 9)
test(unit_place_value(32) == 5)
test(unit_place_value(9) == 9)


# #### Q7. 자연수를 매개 변수로 받아 해당 숫자까지의 팩토리얼을 계산하는 `recursive_factorial` recursive function을 작성하라.

# In[9]:


def recursive_factorial(n):
    factorial = 1
    if n >= 2:
        factorial = n * recursive_factorial(n-1)
    else:
        return factorial
    return  factorial

import math

test(recursive_factorial(5) == math.factorial(5))
test(recursive_factorial(8) == math.factorial(8))
test(recursive_factorial(2) == math.factorial(2))
test(recursive_factorial(10) == math.factorial(10))


# #### Q8. 자연수를 매개 변수로 받아 해당 숫자까지의 팩토리얼을 계산하는 `non_recursive_factorial` non recursive function을 작성하라.

# In[10]:


def non_recursive_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


import math

test(non_recursive_factorial(5) == math.factorial(5))
test(non_recursive_factorial(8) == math.factorial(8))
test(non_recursive_factorial(2) == math.factorial(2))
test(non_recursive_factorial(10) == math.factorial(10))


# #### Q9. 두 자연수를 매개 변수로 받아 최대공약수를 구하는 `my_gcd` function을 작성하라.

# In[11]:


def my_gcd(a, b):
    a = absolute_value(a)
    b = absolute_value(b)
    result = 1
    for i in range(2, min(a,b) + 1):
        while (a%i == 0) and (b%i == 0):
            a = a//i
            b = b//i
            result = result * i
    return  result


import math

test(my_gcd(12, 16) == math.gcd(12, 16))
test(my_gcd(16, 12) == math.gcd(16, 12))
test(my_gcd(9, 6) == math.gcd(9, 6))
test(my_gcd(-12, -38) == math.gcd(-12, -38))


# #### Q10. 임의의 정수가 들어있는 set을 input으로 입력받아, 가장 큰 세 숫자만을 가지고 있는 set을 반환하는 `max_of_three` function을 작성하라.

# In[12]:


def max_of_three(l):
    temp_ls = list(l)
    three_max_ls = []

    for i in range(3):
        three_max_ls.append(max(temp_ls))
        temp_ls.remove(max(temp_ls))

    three_max_set = set(three_max_ls)
    return three_max_set


test(max_of_three({1, 2, 3, 4, 5}) == {3, 4, 5})
test(max_of_three({-100, 42, 32, -4, -1}) == {42, 32, -1})


# #### Q11. 임의의 정수가 들어있는 리스트를 input으로 입력받아, 전부 곱한 결과를 반환하는 `mult_of_list` function을 작성하라.

# In[13]:


def mult_of_list(l):
    result = 1
    for i in range(len(l)):
        result *= l[i]

    return result


test(mult_of_list([1, 2, 3, 4]) == 24)
test(mult_of_list([1, 20, -3, 4]) == -240)
test(mult_of_list([1, 0, -33, 9999]) == 0)


# #### Q12. 임의의 정수가 들어있는 리스트를 input으로 입력받아, 그 중 짝수만을 가진 리스트를 반환하는 `even_filter` function을 작성하라.

# In[14]:


def even_filter(l):
    filtered_l = []

    for i in range(len(l)):
        if l[i] % 2 == 0:
            filtered_l.append(l[i])

    return filtered_l


test(even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8])
test(even_filter([1, 3, 5, 7, 9]) == [])

