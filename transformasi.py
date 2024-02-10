# transform str to Uppercase  or Lowercase

kata = "dicoding"
kata2 = "DICODING"

print(kata.upper())
print (kata2.lower())

print("=====================================")
#Prefix and Suffix
kata3 = "codecodeDicodingcodecode"

print("dicoding         ".rstrip())
print("           dicoding".lstrip())
print("      dicoding        ".strip())
print(kata3.strip("code"))
print("Dicoding Indonesia".startswith("Dicoding"))
print("Dicoding Indonesia".endswith("Indonesia"))

print("=====================================")
#Separate and Join String
print(' '.join(['Indonesia', 'Anniv', 'Ke', '100', '!']))
print('-'.join(['Indonesia', 'Anniv', 'Ke', '100', '!']))
print('Indonesia Anniv Ke 100'.split())
print('''Hi
Indonesia Raya Merdeka
Tanahku Negeri Yang
Kucinta'''.split('\n'))

print("=====================================")
#Replace String Element
string = "Ayo belajar pemrograman di dicoding"
print(string.replace("belajar", "bermain"))

print("=====================================")
#String Checking, return boolean
print('DICODING'.isupper())
print('DICODING'.islower())
print('DICODING'.isalpha())
print('DICODING123'.isalnum())
print('123'.isdigit())
print('          '.isspace())
print('Dicoding Indonesia'.istitle())

print("=====================================")
#String formatting
print('code'.zfill(5))
print('code'.rjust(20))
print('code'.rjust(20,'!'))
print('code'.ljust(10))
print('code'.center(10,'-'))

print("=====================================")
#String literals
#Escape Character as follows:
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash
print('Jum\'at or it\'s nice')
print('I love\t you')
print('I love\n you so much')
print('him or\\and her')

print("=====================================")
#Raw String = print everything
print(r'sagjdbjsf12313243\'55dggs')
print(r'sagjdbjsf123@!#@#$\\5dggs')







