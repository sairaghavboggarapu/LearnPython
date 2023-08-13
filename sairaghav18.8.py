Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #operaters & expressions
>>> str1="good"
>>> str2="morning"
>>> str1+=str2
>>> print(str1)
goodmorning
>>> #urinary operator"+-"
>>> b=17
>>> a=-(b)
>>> print(a);c=-(a);print(c)
-17
17
>>> #bitwise and'&'
>>> 1010111 & 1111010
24994
>>> #bitwise or '|'
>>> 1010101 |1010101
1010101
>>> #bitwise xor '^'
>>> 10101011 ^10101110
101
>>> #bitwise not '~'
>>> ~ 1010101
-1010102
>>> #string manipulation
>>> print("hello i am raghav" *5)
hello i am raghavhello i am raghavhello i am raghavhello i am raghavhello i am raghav
>>> #program that perform addition and multiplication
>>> str1='Hello'
>>> print(str1+'5')
Hello5
>>> print(str1 *2)
HelloHello
>>> #slice opration of a string
>>> str1='python is Easy!!!'
>>> print(str1[0]);print(str1);print(str1[3:9]);print(str1[4:]);print(str1[-1]);print(str1[:6]);print(str1 * 3);print(str1+"ISN't it?");
p
python is Easy!!!
hon is
on is Easy!!!
!
python
python is Easy!!!python is Easy!!!python is Easy!!!
python is Easy!!!ISN't it?
>>> #program to demonstrate operation on tuple
>>> tup1=('a','bc',78,1.254)
>>> tup2=('d',78)
>>> print(tup1;)
SyntaxError: invalid syntax
>>> print(tup1);print(tup1[0]);print(tup1[1:3]);print(tup1[2:]);print(tup1* 2);print(tup1+tup2);
('a', 'bc', 78, 1.254)
a
('bc', 78)
(78, 1.254)
('a', 'bc', 78, 1.254, 'a', 'bc', 78, 1.254)
('a', 'bc', 78, 1.254, 'd', 78)
>>> #program to demonstrate operation on list
>>> list1=['a','bc',78,1.25]
>>> list2=['d',75]
>>> print(list1);print(list[0]);print(list1[1:3]);print(list1[2:]);print(list 1*2);print(list1 + list2);
SyntaxError: invalid syntax
>>> print(list1);print(list[0]);print(list1[1:3]);print(list1[2:]);print(list1*2);print(list1+list2);
['a', 'bc', 78, 1.25]
list[0]
['bc', 78]
[78, 1.25]
['a', 'bc', 78, 1.25, 'a', 'bc', 78, 1.25]
['a', 'bc', 78, 1.25, 'd', 75]
>>> 