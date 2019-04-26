#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random as rn
from copy import copy
from re import match
import re


# In[2]:


def ASCIItoBinary(data):
    output = (''.join(format(ord(x), 'b') for x in data))
    return output


# In[3]:


def string2list(string, size, num_blocks):
    out = []
    for i in range(num_blocks):
        out.append(string[i*size:i*size+size])
    return out


# In[4]:


def list2string(list, size):
    out = ''
    for x in list:
        if(len(x) < size): x = '0'*(size - len(x)) + x
        out += x
    return out


# In[5]:


def check_binary(input):
    for i in range(len(input)):
#         if(input[i]!='1' and input[i] != '0'):
        if not(match("[01]+", input[i])):
            print("at i = ", i)
            print("input must be a string of 0 or 1!")
            return 0
    return 1


# In[6]:


def unreliable_transmission(input, p):
    output = ""
    if not(check_binary(input)):
        return -1
    for i in range(len(input)):
#         output = copy(input)
        if rn.random() < p:
            output += str(rn.choice([0,1]))
        else: output += input[i]
    return output


# In[7]:


def parity_gen(input, type, size=""):
    if not(check_binary(input)):
        return -1
    if(len(input) < 9):
        print("input length should be at least 9.")
        return -1
    if(type > 3 or type < 0):
        print("type must be between 0 and 3.")
        return -1
    
    if(type==0 or type==1):
        output = copy(input)
        prev = 0
        for i in range(len(input)):
            cur = input[i]
            result = int(prev) ^ int(cur)
            prev = int(result)
        output += str(int(result if type==0 else result ^ 1))
            
    else:
        output = np.zeros(0, dtype=int)
        if not(match("[\d]+x[\d]+", size)):
            print("size parameter should be written as '<number>x<number>'.")
            return -1
        else: m, n = re.split('x', size); m, n = int(m), int(n)
        mat = np.array(list(input), dtype=int)
        mat = mat.reshape([m, n])
        for i in range(m):
            prev = 0
            for j in range(n):
                cur = mat[i,j]
                result = int(prev) ^ int(cur)
                prev = int(result)
            out = np.append(mat[i,:], int(result if type==2 else result ^ 1))
            output = np.append(output, out)
        out = np.zeros(0, dtype=int)
        mat = output.reshape([m, n+1])
        for j in range(n+1):
            prev = 0
            for i in range(m):
                cur = mat[i, j]
                result = int(prev) ^ int(cur)
                prev = int(result)
            out = np.append(out, int(result if type==2 else result ^ 1))
        output = np.append(output, out)
#         output = output.reshape([m+1,n+1])
        a = ""
        for i in range(output.size):
            a += str(output[i])
        output = a

    return output


# In[8]:


def parity_check(input, type, size=""):
    if not(check_binary(input)):
        return -1
    if(len(input) < 9):
        print("input length should be at least 9.")
        return -1
    elif(type > 3 or type < 0):
        print("type must be between 0 and 3.")
        return -1
    
    if(type==0 or type==1):
        prev = 0
        for i in range(len(input)):
            cur = input[i]
            result = int(prev) ^ int(cur)
            prev = int(result)
        if(type==0): result = result^1
            
    else:
        result = 1
        if not(match("[\d]+x[\d]+", size)):
            print("size parameter should be written as '<number>x<number>'.")
            return -1
        else: m, n = re.split('x', size); m, n = int(m), int(n)
        mat = np.array(list(input), dtype=int)
        mat = mat.reshape([m, n])
        for i in range(m-1):
            prev = 0
            for j in range(n):
                cur = mat[i,j]
                result = int(prev) ^ int(cur)
                prev = int(result)
            result = int(result if type==3 else result ^ 1)
            if not(result): break
        if(result):
            for j in range(n):
                prev = 0
                for i in range(m):
                    cur = mat[i, j]
                    result = int(prev) ^ int(cur)
                    prev = int(result)
                result = int(result if type==3 else result ^ 1)
                if not(result): break
        
    return "The validity of codeword is " + str(bool(result))


# In[9]:


def mod2div(input, divisor):
    countXOR = len(divisor)
    temp = input[0:countXOR]
    while countXOR < len(input):
        if(temp[0] == '1'):
            temp = xor(divisor, temp) + input[countXOR]
        else: temp = xor('0'*countXOR, temp) + input[countXOR]
        countXOR += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else: temp = xor('0'*countXOR, temp)
    output = temp
    return output


# In[10]:


def xor(a,b):
    output = []
    for i in range(1, len(b)):
        if a[i] == b[i]: 
            output.append('0') 
        else: 
            output.append('1') 
   
    return ''.join(output) 


# In[11]:


def CRC_gen(input, divisor):
    if not(check_binary(input)):
        return -1
    if not(0 <= int(divisor) < 5):
        print("divisor can only be 0-4!")
        return -1

    div = "11111"
    if(divisor==1): div = "111010101"
    elif(divisor==2): div = "10100000000000011"
    elif(divisor==3): div = "11000000000000101"
    elif(divisor==4): div = "1100000000101000100000001"
    elif(divisor==5): div = "100000100110000010001110110110111"

    app_input = input + '0'*(len(div) - 1)
    output = input + mod2div(app_input, div)
    return output


# In[12]:


def CRC_check(input, divisor):
    if not(check_binary(input)):
        return -1
    if not(0 <= int(divisor) < 5):
        print("divisor can only be 0-4!")
        return -1

    div = "11111"
    if(divisor==1): div = "111010101"
    elif(divisor==2): div = "10100000000000011"
    elif(divisor==3): div = "11000000000000101"
    elif(divisor==4): div = "1100000000101000100000001"
    elif(divisor==5): div = "100000100110000010001110110110111"
        
    app_input = input + '0'*(len(div) - 1)
    output = mod2div(app_input, div)
    if(output==('0'*(len(div) - 1))):
       result = True
    else: result = False
        
    return "The validity of the codeword is " + str(result)


# In[13]:


def Checksum_gen(input, size, num_block):
    output = list2string(input, size)
    if not(check_binary(input)):
        return -1
    
    sum = 0
    for i in range(num_block):
        sum = sum + int(input[i], 2)
        
    temp = sum % (pow(2,size) - 1)
    if temp==0: temp = pow(2, size) - 1
    temp_bi = "{0:b}".format(temp)
    if(len(temp_bi) < size): temp_bi = '0'*(size - len(temp_bi)) + temp_bi
    result = ""
    for i in range(len(temp_bi)):
        result = result + str(int(temp_bi[i])^1)
    output += result
    return output


# In[52]:


def Checksum_check(input, size, num_block):
    if not(check_binary(input)):
        return -1
    
    sum = 0
    for i in range(num_block):
        sum = sum + int(input[i], 2)
        
    temp = sum % (pow(2,size) - 1)
    if temp==0: temp = pow(2, size) - 1
    temp_bi = "{0:b}".format(temp)
    if(len(temp_bi) < size): temp_bi = '0'*(size - len(temp_bi)) + temp_bi
    complement = ""
    for i in range(len(temp_bi)):
        complement = complement + str(int(temp_bi[i]) ^ 1)
    if(match("0{"+str(size)+"}", complement)):
        result = True
    else: result = False
    return "The validity of the codewords is " + str(result)


# In[15]:


def Hamming_gen(input):
    
    reverse_input = input[::-1]
    
    if not(check_binary(reverse_input)):
        return -1
    
    num_of_added_bit = 0
    num_bits = len(reverse_input)
    
    while 2.**num_of_added_bit <= num_bits:
        num_of_added_bit += 1

    out = list()
    i=j=k=0
    
    while i < num_of_added_bit + num_bits:
        if i == (2.**j - 1):
            out.insert(i, "0")
            j += 1
        else:
            out.insert(i, reverse_input[k])
            k += 1
        i+=1

    i = 0 
    k = 0
    while i <= num_of_added_bit:
        k = 2.**i
        j = 1
        total = 0
        while j*k - 1 <len(out):
            if(j*k -1 == len(out)-1):
                lower_index = j*k -1
                temp = out[int(lower_index):len(out)]
            elif((j+1)*k -1 >= len(out)):
                lower_index = j*k -1
                temp = out[int(lower_index):len(out)] 
            elif((j+1)*k -1<len(out)-1):
                lower_index = (j*k)-1
                upper_index = (j+1)*k -1
                temp = out[int(lower_index):int(upper_index)]

            total += sum(int(e) for e in temp) 
            j += 2 
        if total%2 > 0:
            out[int(k)-1] = '1'
        i+=1
        
    return ''.join((x) for x in out[::-1])


# In[53]:


def Hamming_check(input):
    num_o_bits = 0
    i = 0
    while 2.**i <= len(input):
        num_o_bits+=1
        i+=1
    i = 0
    out = list(input[::-1])
    error_bit = 0
    while i < num_o_bits:
        k=2.**i
        j=1
        total=0
        while j*k -1 < len(out):
            if j*k -1 == len(out) - 1:
                lower_index = j*k - 1
                temp = out[int(lower_index):len(out)]
            elif (j+1)*k - 1 >= len(out):
                lower_index = j*k - 1
                temp = out[int(lower_index):len(out)]
            elif (j+1)*k - 1 < len(out) - 1:
                lower_index = (j*k) - 1
                upper_index = (j+1)*k -1
                temp = out[int(lower_index):int(upper_index)]

            total+= sum(int(e) for e in temp)
            j+=2
        if total%2 > 0:
            error_bit += k 
        i+=1
    if error_bit>=1:
        output = "There is error in bit no. " + str(len(out) - int(error_bit) + 1)
    else:
        output = "There is no error!"

    return output


# In[61]:


def declist2bilist(listt):
    out = list()
    for i in listt:
        out.append("{0:b}".format(i))
    return out

