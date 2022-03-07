#!/usr/bin/env python
# coding: utf-8

# # Q1) Reverse a given integer number  [ input:76542 ,  output: 24567]

# In[1]:


def reverse(num):
    '''
    reverse any integer
    convert to integer, then reverse and then convert back to intger again
    '''
    num_char = str(num)
    num_char = num_char[::-1]
    return int(num_char)
reverse(1234)
reverse(76542)


# # Q2) Write a python program to find the second largest number in a List

# In[2]:


def second_largest(list_num):
    '''
    function to return second largest numbers in a list
    order the list in descending order, and then return the second largest number
    '''
    list_num.sort(reverse=True)
    return list_num[1]
second_largest([1, 4, 2, 4, 5, 6, 9, 7])


# # Q3) Write a python program to calculate the number of words and the number of characters present in a string

# In[3]:


def word_char_counter(string):
    '''
    get the word and character count in a string
    to get word count: divide the string, using space as separator, return the length of new list
    char count : use the len function
    '''
    return len(string.split(sep=" ")), len(string)

word_char_counter("This is Python")


# # Q4) Write a program to compute prime factors of an integer

# In[4]:


def find_prime_factors(integer):
    '''
    find the prime factors of an integer
    divide the integer in a while loop, to get all the prime factors
    divide till half of integer
    '''
    range_to_look = int(integer/2)
    list_prime_factors = []
    rem_number = integer
    for i in range(2, range_to_look):
        while((rem_number % i) == 0):
              if (rem_number % i == 0):
                    list_prime_factors.append(i)
                    rem_number = rem_number / i
    
    # if number is prime itself
    if(len(list_prime_factors) == 0):
        list_prime_factors.append(integer)
    return list_prime_factors
find_prime_factors(213)
find_prime_factors(223)


# In[5]:


find_prime_factors(2)


# # Q5) Write a python program to find the fibonacci series using recursion

# In[6]:


def recursive_fibonacci(length, fib_series=[]):
    
    if(len(fib_series) == 0):
        fib_series = [0, 1]
        recursive_fibonacci(length, fib_series)
    else:
        len_fib_series = len(fib_series)
        fib_series.append(fib_series[len_fib_series-2] + fib_series[len_fib_series-1])
        if(len(fib_series) >= length):
            return fib_series[0:length]
        else:
            recursive_fibonacci(length, fib_series)
    return fib_series[0:length]
recursive_fibonacci(10)


# In[ ]:




