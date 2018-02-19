# name = input("What is your name?" )
# print("Thank you, " + name)
# def stupidify(word):
#     return "stupid " + word
# # print("Happy Birthday")
# print("Hi, " + stupidify(name))

#input is hello
#output should be a = 0, b = 0 ... e = 1 ... h = 1 ... l = l


# age = int(input("what is your age"))
# print("thankyou,")
# year = int(input("what year is it?"))
# print("you were born in " + str(year - age))

# total = float(input("what is your total ballance?"))
# print("your total ballance with tax is" + str(total * 1.07))

# while True:
#     print("Poop")

# num = 0
# while num < 10:
#     print("Poop " + str(num))
#     num = num + 1

# name1 = ""
# name2 = "1"
# while name1!=name2:
#     name1 = input("Name 1? ")
#     name2 = input("Name 2? ")

# num = 10
# while num > 0:
#     print("" + str(num))
#     num-=1

# Using a while loop
# Ask for prices until a price of 0 is entered, 
# then print the total
# price = 1
# total = 0
# while price != 0:
#     price = float(input("what is the price?"))
#     print("" + str(price))
#     total = price + total
# print(total)


# family = ""
# name = " "
# while name != "":
#     name = input("what is a family members name?")
#     print("" + name)
#     family = name + " " + family
# print(family)

# family = []
# name = " "
# while name !="":
#     name = input("What is a name?" )
#     family.append(name)
# for person in family:
#     print(person)

# for num in range(1,6):
#     print("*" * num)


# import random
# number = 0
# guess = random.randint(1, 200)

# while True:
#     number = int(input("give me a number!"))
#     if number < guess:
#         print("too low!")
#     if number > guess:
#         print("too high!")
#     if number == guess:
#         print("nice, you got it right!")    
#         break



# family = ['chris',  'caroline', 'joe', 'bart', 'sue', 'mary', 'margret', 'margret']
# print(family)
# for person in family:
#     if person[2] == 'r':
#         print(person)

# numbers = []
# total = 0
# while True:
#     entry = input("Give me a number")
#     if entry.isdigit():
#         number = int(entry)
#     else:
#         break
#     numbers.append(number)
# total = sum(numbers)
# print(numbers)
# print(total)

# numberlist = [4, 6, 78, 49]
# print(numberlist)
# for number in numberlist:
#     print(number * 2)

# hello = "hello"
# caroline = "caroline"
# print(hello + caroline)
# print(caroline + hello)

#Given set of rules, generate all syntatic words under 10 characters
#rules 

# _end = '_end'
# def make_trie(dic):
#      root = dict()
#      for word in dic:
#          current_dict = root
#          for letter in word:
#              current_dict = current_dict.setdefault(letter, {})
#          current_dict[_end] = _end
#      return root

# dictionary = open('input/en_US.dic')
# words = list()
# for line in dictionary:
#     word = line.split('/')[0].strip()
#     words.append(word)
    
# # l = make_trie(words)
# while True:
#     pos0 = int(input('First position'))
#     pos1 = int(input('Second position'))
#     let0 = input('First letter')
#     let1 = input('Second letter')
#     length = int(input('Word length'))
#     for word in words:
#         if len(word)==length:
#             if word[pos0-1] == let0 and word[pos1-1] == let1:
#                 print(word)


# for word in words:
#     if word[0].upper() == 'L' and len(word) == 7:
#         print(word)
# for word in words:
#     if word[0].upper() == "A" and word[-1].upper() == "Z":
#         print(word)
# def word_Value(word):
#     carrier = 0
#     for letter in word:
#         if letter.isalpha():
#             carrier += ord(letter.lower()) - 96
#     return carrier
# words.sort(key = word_Value)
# print(words)
# print(word_Value(words[-1]))
# noEs = list()
# for word in words: 
#     if 'e' not in word:
#         noEs.append(word)
# noEs.sort(key = len)
# print(noEs)

# def numDubs(word):
#     numDubs = 0
#     for i, c in enumerate(word):
#         if c == word[i-1]:
#             numDubs+=1
#     return numDubs
            
# words.sort(key=numDubs)
# print(words)


from PIL import Image
#Read image
im = Image.open( 'input/apollo2.jpg' )
#Display image
# r,g,b = im.split()
# r = r.rotate(10)
# b = b.rotate(-5)
# b = b.point(lambda i: i*2)
# new = Image.merge("RGB",(r,g,b))
# new.show()

#create a pixel access object
pix = im.load()
width, height = im.size

pix_list = list()
pix_dic = dict()

for x in range(width):
    for y in range(height):
        pixel = pix[x,y]
        # pix_list.append((pixel,(x,y)))
        loc = (x,y)
        las = pix_dic.get(pixel,[])
        las.append(loc)
        pix_dic[pixel] = las
    # print('x at ', x)

# pix_list.sort()
# pix_dic.sort()
keys = list(pix_dic)
keys.sort()

lastred = 0
lastgreen = 0
lastblue = 0

for r,g,b in keys:
    loc_list = pix_dic[(r,g,b)]
    lastgreen = g
    lastred = r
    lastblue = b
    stepb = int(b / len(loc_list))
    stepg = int(g / len(loc_list))
    stepr = int(r / len(loc_list))
    
    for loc in loc_list:
        if lastblue > 255:
            lastblue = 0
        lastgreen+=stepg
        lastblue+=stepb
        lastred+=stepr
        if lastred > 255:
            lastred = 0
        if lastgreen > 255:
            lastgreen = 0
        pix[loc[0],loc[1]] = (lastred, lastgreen, lastblue)

im.save('edited.jpg')