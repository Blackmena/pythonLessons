# 15
# with open("test.txt","w") as f:
#     f.write("hello world")
#
# with open("test.txt","r") as f:
#     koo = f.read().split()
#     del koo[1]
#     print(koo)
# 16
# with open("test.txt","r") as file:
#     result = file.readline()
#     result = result.replace(" ","")
#     print(result)
# with open("test.txt","w") as file:
#     file = file.write(result)


# 17
# with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
#     lines1 = f1.readlines()
#     lines2 = f2.readlines()
#
# result = []
#
# for i in range(len(lines1)):
#     result.append(lines1[i].rstrip("\n"))
#     if i < len(lines2):
#         result.append(lines2[i].rstrip("\n"))
#
# with open("merged.txt", "w") as out:
#     out.write("\n".join(result))
#
# print("✅ Fayllar birlashtirildi! Natija merged.txt faylida.")

# 18
# k = 3
# with open("numbers.txt", "w") as f:
#     numbers = f.write("Java numbers Karma power menu bermuda")
#
# with open("numbers.txt", "r") as file:
#     file = file.read().split()
#
# noid = [word for word in file if len(word) <= k]
# print(noid)

# 19
# with open("magic.txt", "w") as file:
#     file.write("MaGiC")
#
# with open("magic.txt", "r") as file:
#     result = file.read()
#     loop = []
#     for i in result:
#         if i.isupper():
#             i = i.lower()
#             loop.append(i)
#         elif i.islower():
#             i = i.upper()
#             loop.append(i)
# with open("magic.txt", "w") as file:
#     file.write(str(loop))

# 20
# with open("text.txt", "w") as f:
#     file = f.write("hello   nwkfjwlni ewf bwe fb   ewibuew")
#
# with open("text.txt", "r") as f:
#     text = f.read()
#
# new_text = " ".join(text.split())
#
# with open("text.txt", "w") as f:
#     f.write(new_text)
# print(f)

# 21

# def myfunction():
#     with open("text.txt", "r") as file:
#         linux = file.readlines()

#     if len(linux) <= 3:
#         new_lines = linux
#     else:
#         new_lines = linux[:-3]

#     with open("newlines.txt", "w")as file:
#         file.writelines(new_lines)
# myfunction()

# 22

# def myfunction():
#     with open("text.txt", "r") as file:
#         linux = file.readlines()

#     if len(linux) <= 10:
#         new_lines = linux
#     else:
#         new_lines = linux[:-3]

#     with open("newlines.txt", "w")as file:
#         file.writelines(new_lines)
# myfunction()

# 23

# k = int(input("K= "))
# with open("input.txt", "w") as file:
#     line = file.write(" eb ebw hfbew jf ew eh bwejbewh webhbwekblk")

# with open("input.txt", "r") as file:
#     lines = file.readlines() 

#     result = lines[-k:] if len(lines) >= k else lines

# with open("output.txt", "w") as menu:
#     menu.writelines(result)

# 24

# with open("input.txt", "r") as new:
#     content = new.read()

# paragraph = content.split("\n\n")
# paragraph_count = len([p for p in paragraph if p.strip()])

# print(f"Abzaslar soni {paragraph_count}")

# 25

# K = int(input("K = "))

# with open('input.txt', 'r') as f:
#     content = f.read()

# paragraphs = content.split('\n\n')
# filtered_paragraphs = [p for p in paragraphs if p.strip()]

# if 1 <= K <= len(filtered_paragraphs):
#     del filtered_paragraphs[K-1]
#     result = '\n\n'.join(filtered_paragraphs)
    
#     with open('input.txt', 'w') as f:
#         f.write(result)
#     print("Abzas o'chirildi")
# else:
#     print("Bunday abzas mavjud emas")

# 27

# with open("input.txt", "r") as file:
#     nim = file.readlines()

# paragraph = 0
# in_paragraph = False

# for i in nim:
#     if i.startswith("   ") and i.strip():
#         paragraph += 1
#         in_paragraph = True
#     elif not i.strip():
#         in_paragraph = False

# print(paragraph)

# 29

# with open("input.txt", "r") as file:
#     menu = file.read()

# import re
# words = re.findall(r'\b\w+\b', menu)

# if words:
#     longest_word = max(words, key=len)
#     print(f"Eng uzun so`z {longest_word}")
# else:
#     print("so`z topilmadi")

# 30

# with open('input.txt', 'r') as f:
#     content = f.read()

# import re
# words = re.findall(r'\b\w+\b', content)

# if words:
#     min_length = min(len(word) for word in words)
#     shortest_words = [word for word in words if len(word) == min_length]
#     last_shortest = shortest_words[-1]
#     print(f"Eng qisqa oxirgi so'z: {last_shortest}")
# else:
#     print("So'z topilmadi")

# 31
# K = int(input("K = "))

# with open('input.txt', 'r') as f:
#     content = f.read()

# import re
# words = re.findall(r'\b[a-zA-Z]+\b', content)

# words_with_length_k = [word for word in words if len(word) == K]

# with open('output.txt', 'w') as f:
#     if words_with_length_k:
#         for word in words_with_length_k:
#             f.write(word + '\n')

# 32
# C = input("C harfini kiriting: ").upper()

# with open('input.txt', 'r', encoding='utf-8') as f:
#     content = f.read()

# import re
# words = re.findall(r'\b[a-zA-Z]+\b', content)

# words_starting_with_C = [word for word in words if word.upper().startswith(C)]

# with open('output.txt', 'w', encoding='utf-8') as f:
#     for word in words_starting_with_C:
#         f.write(word + '\n')

# 33

# C = input("C harfini kiriting: ").lower()

# with open('input.txt', 'r', encoding='utf-8') as f:
#     content = f.read()

# import re
# words = re.findall(r'\b[a-zA-Z]+\b', content)

# words_starting_with_C = [word for word in words if word.lower().startswith(C)]

# with open('output.txt', 'w', encoding='utf-8') as f:
#     for word in words_starting_with_C:
#         f.write(word + '\n')

# 34

# with open('input.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()

# WIDTH = 50
# result_lines = []

# for line in lines:
#     line = line.rstrip('\n')
#     if line.strip():
#         spaces_needed = WIDTH - len(line)
#         if spaces_needed > 0:
#             justified_line = line + ' ' * spaces_needed
#         else:
#             justified_line = line[:WIDTH]
#     else:
#         justified_line = ''
#     result_lines.append(justified_line + '\n')

# with open('output.txt', 'w', encoding='utf-8') as f:
#     f.writelines(result_lines)