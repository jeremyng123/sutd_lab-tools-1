import hashlib as hl
import random as r

l = 'abcdefghijklmnopqrstuvwxyz0123456789'
my_answers = open("output.txt", 'r')
plaintexts = []
for line in my_answers:
    words = line.split()
    if len(words) >= 3:
        plaintexts.append(words[0])
my_answers.close()

output_dict=""
output=""

r.seed("3")
for word in plaintexts:
    newword= word+l[r.randint(0,len(l)-1)]
    newhash = hl.md5(newword.encode()).hexdigest()
    output_dict += f"{newword} = {newhash}\n"
    output += f"{newhash}\n"



salt6txt_dic = open("salted6_dic.txt",'w')
salt6txt_dic.write(output_dict)
salt6txt = open("salted6.txt",'w')
salt6txt.write(output)