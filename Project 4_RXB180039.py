#!/usr/bin/env python
# coding: utf-8

# The Romans represented numbers using the numerals ``I``, ``V``, ``X``, ``L``, ``C``, ``D``, and ``M``. These numerals represent the following numbers:
# 
# |Roman Numeral	|Hindu-Arabic Equivalent|
# |:---|:---|
# |I	|1|
# |V	|5|
# |X	|10|
# |L	|50|
# |C	|100|
# |D	|500|
# |M	|1000|
# 
# 
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
# 1. Repeating a numeral up to three times represents addition of the number. For example, III represents 1 + 1 + 1 = 3. 
# 2. Only I, X, C, and M can be repeated; V, L, and D cannot be, and there is no need to do so.
# 3. Writing numerals that decrease from left to right represents addition of the numbers. For example, LX represents 50 + 10 = 60 and XVI represents 10 + 5 + 1 = 16.
# 4. To write a number that otherwise would take repeating of a numeral four or more times, there is a subtraction rule. 
# 5. Writing a smaller numeral to the left of a larger numeral represents subtraction. For example, IV represents 5 - 1 = 4 and IX represents 10 - 1 = 9. To avoid ambiguity, the only pairs of numerals that use this subtraction rule are
# 
# |Roman Numeral	|Hindu-Arabic Equivalent|
# |:---------------|:-----------------------|
# |IV	|4 = 5 - 1|
# |IX	|9 = 10 - 1|
# |XL	|40 = 50 - 10|
# |XC	|90 = 100 - 10|
# |CD	|400 = 500 - 100|
# |CM	|900 = 1000 - 100|
# 
# Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
# 
# For example, it would appear that there are at least six ways of writing the number sixteen:
# ```
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
# ```
# However, according to the rules, only ``XIIIIII`` and ``XVI`` are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
# 
# In this project, you will read a roman numeral from the user. First, you need to check if the number if in a valid form according to the rules posted above. Then convert it to the minimal representation. It's essential to modularize your code, and you are free to use either for or while loop. You are not allowed to use any of the Python structures that are not taught so far. 

# In[1]:


def ValidRoman(roman_num):
    """Validating if the strings entered are correct"""
    
    # Converting the letters to upper case (if any small letters are preset)
    global roman
    roman = roman_num.upper()
    print('The Roman Numeral entered is:',roman_num)
    
    # Separating the letters
    ind_ch = list(roman)
                
    # Creating an array of valid roman numerals to be considered    
    valid = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    for character in ind_ch:        
        if character not in valid:
            print('Error! Please enter the displayed characters only.')
            return False
    return True

def Repeat(roman):
    """This function if any character other than I, X, C and M is repeated"""
    
    ind_ch = list(roman)
    
    for letter in ind_ch:
        if letter not in repeat and roman.count(letter)>1:                        
            return False
    return True

def DescRule(roman):
    """This function will check if the characters are in descending order except a few exceptions"""
    
    ind_ch = list(roman)
    
    list_temp = []
    
    invalidFlag = False
    c = 0
    while c < len(ind_ch):
            #print('for c:',c)
            #print(roman[c:c+2])
            while roman[c:c+2] in combo:
                #print('while c:',c)
                if len(list_temp) == 0 or list_temp[-1] >= combo[roman[c:c+2]]:
                    list_temp.append(combo[roman[c:c+2]])
                    c = c + 2
                else:
                    print('Invalid')
                    invalidFlag = True
                    return False
                #print('List_temp:',list_temp)
                #print('c:',c)
            if c == len(ind_ch):
                break
            
            #print('Last ele:',list_temp[-1])
            #print('Char:', ind_ch[c])
            #print('Value of char:',value[ind_ch[c]])
            if len(list_temp) == 0 or list_temp[-1] >= value[ind_ch[c]]:
                list_temp.append(value[ind_ch[c]])
            else:
                return False
            c+=1

    return True

def Rules(roman):
    """This function validates the specified rules for the Roman Numeral to be valid"""
    
    ind_ch = list(roman)
    
    global sum_roman
    
    sum_roman = 0
    ch = 0
    while ch < len(ind_ch):
    
        count = 1
        
        
        while roman[ch:ch+2] in combo:
            sum_roman = sum_roman + combo[roman[ch:ch+2]]
            ch = ch + 2
    
    
        if ch == len(ind_ch):
            break
    
        while ch < len(ind_ch)-1 and ind_ch[ch] == ind_ch[ch+1]:
            count +=1
            ch += 1
    
        #if count % 3 == 0:
            #sum_roman = sum_roman + value[ind_ch[ch]] * count
        #else:
        if count <=9:
            sum_roman = sum_roman + value[ind_ch[ch]] * count
        else:
            print('Error!')
            return False
            break      
        
        if ch == len(ind_ch)-1:
            break
    
        ch += 1
    print('Sum:',sum_roman)
    return sum_roman
    
def RomanRep(sum_roman):
    """This function will return the minimal/official representation of the number"""
    b = 0
    roman_rep = ""
    
    roman_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV','I']
    integer_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
    
    while sum_roman > 0:
        if sum_roman >= integer_values[b]:
            sum_roman = sum_roman - integer_values[b]
            roman_rep += roman_values[b]
        else:
            b = b + 1

    print('The minimal representation is:', roman_rep)
    return roman_rep


s = False

repeat = ['I','X','C','M']

value = {'I':1, 'V':5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M':1000}

combo = {'IV': 4, 'IX':9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

while not s:
    roman_num = input('Enter the Roman Numerals between I,V,X,L,C,D,M:')
    if roman_num.isnumeric():
        print('Error! The input has numeric characters!')
        continue
    s = ValidRoman(roman_num)
    if s == False:
        continue
    s = Repeat(roman)
    if s == False:
        print('Error!Only characters I,X,C and M can be repeated.')
        continue
    s = DescRule(roman)
    if s == False:
        continue
    s = Rules(roman)
    if s == False:
        continue
    s = RomanRep(sum_roman)      


# In[ ]:




