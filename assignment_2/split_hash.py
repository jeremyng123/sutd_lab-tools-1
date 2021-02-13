import hashlib as hl
import random as r

dlmt = ": \n\r\t"
l = 'abcdefghijklmnopqrstuvwxyz0123456789'
hash_targets = open("hashes.txt", 'r')
filestr = ''
plaintexts = {'weak':[], 'moderate':[], 'strong':[]}
for line in hash_targets:
    words = line.strip(dlmt).split('.')
    if len(words) == 1 and words[0] != '':
        filestr = words[0].lower()
    elif len(words) >= 2:
        plaintexts[filestr].append(words[-1])
hash_targets.close()

output_weak=""
output_moderate=""
output_strong=""

for weak in plaintexts['weak']:
    output_weak += weak + '\n'
for moderate in plaintexts['moderate']:
    output_moderate += moderate + '\n'
for strong in plaintexts['strong']:
    output_strong += strong + '\n'

outtxt_weak = open("weakhash.txt",'w')
outtxt_weak.write(output_weak)
outtxt_moderate = open("moderatehash.txt",'w')
outtxt_moderate.write(output_moderate)
outtxt_strong = open("stronghash.txt",'w')
outtxt_strong.write(output_strong)

outtxt_weak.close()
outtxt_moderate.close()
outtxt_strong.close()
