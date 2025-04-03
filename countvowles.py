def count_vowels(s):
    s = s.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
    
print(count_vowels("Hello World"))
print(count_vowels("python"))
print(count_vowels("Beautiful Day"))
