# # HNYfile = open("FileHandling/HNY.txt", 'a')

# # HNYfile.write("\nHappy New Year for tomorrow")

# # HNYfile.close()

# HNYfile = open("FileHandling/HNY.txt", 'r')
# # content = HNYfile.read()
# # contentLine = HNYfile.readline()
# print(HNYfile.readline(), end='')
# # print(HNYfile.readline(), end='')

# print(HNYfile.tell())
# HNYfile.seek(80)
# # print(HNYfile.readline(), end='')
# print(HNYfile.read(), end='')
# # contentList = HNYfile.readlines()
# HNYfile.close()

# # print(content)
# # print(contentLine)
# # print(contentList)

file = open('FileHandling/HNY.txt', 'a')
file.write("\nWe apended this later")

li = ['\nWe\n', 'Are\n', 'Going\n', 'picknic\n']

file.writelines(li)
file.close()
