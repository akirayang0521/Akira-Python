def func1():
    # calculate the total length of words, ignore word like 'the'. All inputs are lower cases.
    # this is the original function, do not change this function.
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_lengths = []
    for word in words:
        if word != "the":
            word_lengths.append(len(word))
    return sum(word_lengths)

def func1_list_comprehension():
    # rewrite the 'func1' below in list comprehension to achieve the same functionality
    # remove the 'pass' when you start coding, since 'pass' is only a placeholder
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_lengths = [len(word) for word in words if word != "the"]
    return sum(word_lengths)

def func2():
    # form a new list, with only positive numbers in it
    # this is the original function, do not change this function.
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    newlist = []
    for n in numbers:
        if n > 0:
            newlist.append(n)
    return newlist

def func2_list_comprehension():
    # rewrite the 'func2' below in list comprehension to achieve the same functionality
    # remove the 'pass' when you start coding, since 'pass' is only a placeholder
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    newlist = [n for n in numbers if n > 0]
    return newlist

def func3_square():
    # use list comprehension to generate a new list of x ** 2,  (x = 1, 2, 3, ... 9, 10)
    # return this new list, it should look like [1, 4, 9, ...]
    return [x ** 2 for x in range(1,11)]

def func4_cube_odd():
    # use list comprehension to generate a new list of x * x * x, ( x = 1, 2, 3... 19, 20)
    # only use the odd numbers like 1,3,5.
    # Return a new list containing the cube of odd numbers like [1, 27, 125, ...]
    return [x ** 3 for x in range(1,21) if x % 2 != 0]

def func5_vowel():
    # given a string 's'
    # use list comprehension to generate a new list, that only consists of the vowel letters: AEIOU, from string 's'
    # note, all input strings are capital letter.  Expect to return a new list of ['A', 'I', 'A', 'E', ....]
    s = 'MATH IS A GREAT SUBJECT BUT NOT EVERYONE LOVES IT'
    vowels = 'AEIOU'
    return [letter for letter in s if letter in vowels]



print('original func1 returns: %s, \n     new func1 returns: %s.' % (func1(), func1_list_comprehension()))
print('original func2 returns: %s, \n     new func2 returns: %s.' % (func2(), func2_list_comprehension()))
print('func3_square returns: %s' % func3_square())
print('func4_cube_odd returns: %s' % func4_cube_odd())
print('func5_vowel returns: %s' % func5_vowel())

