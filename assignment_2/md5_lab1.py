import hashlib as hl
import time
import argparse

def run():
  # STUDENT_ID=3
  # FILENAME=str(STUDENT_ID)+ '.txt'

  # WORDS5 = "words5.txt"

  hashtargets = []
  hashes = open(args.input, 'r')
  for hashline in hashes:
    hashtargets.append(hashline.strip())
  hashes.close()

  tried = []
  answers = {}
  words = open(args.with_dict, "r")
  start = time.time()
  for line in words:
    # print(line.strip())
    hm = hl.md5(line.strip().encode()).hexdigest()
    if hm in hashtargets:
      answers[line.strip()] = hm
      # try:
      #   hashtargets.remove(hashline.strip())
      # except:
      #   print('dk why value not in list')
      #   print(f"{hashtargets}")
      print(f"{line} = {hm}")
    tried.append(line)
  words.close()
  exhausted_dict_time = time.time()-start


  l = 'abcdefghijklmnopqrstuvwxyz0123456789'
  alltries=[]
  index = 0
  for a in range(len(l)):
    for b in range(len(l)):
      for c in range(len(l)):
        for d in range(len(l)):
          for e in range(len(l)):
            sometry = l[a]+l[b]+l[c]+l[d]+l[e]
            alltries.append(sometry)
  print("start brute force")
  for element in alltries:
    hm = hl.md5(element.encode()).hexdigest()
    if hm in hashtargets:
      if element not in answers.keys():
        print(answers.keys())
        answers[element] = hm
      else:
        continue
      # hashtargets.remove(hm)
      print(f"{element} = {hm}")
      if len(hashtargets) == 0:
        break
    index+=1
    if index%1000000==0:
      print(f"tried: {index}times\nenumerating: {element}\nanswers foundso far: {len(answers.keys())}")
  
  write_to_output = ""
  for k,v in answers.items():
    write_to_output += "{} = {}\n".format(k,v)
  timetaken = time.time()-start

  print(f"total time taken: {timetaken}")
  print(f"exhausted dict time taken: {exhausted_dict_time}")
  write_to_output += str(timetaken)+"\n"
  write_to_output += str(exhausted_dict_time)+"\n"
  output = open(args.output, 'w')
  output.write(write_to_output)
  output.close()
  
  
  
  print(answers)
    
  #           # print(sometry)
  #           if sometry in tried:
  #             continue
  #           hm = hl.md5(sometry.encode()).hexdigest()
  #           if hm in hashtargets:
  #             answers[sometry]=hm
  #             print(f"{line} = {hm}")
  #           tried.append(sometry)
  #           index+=1
  #           if len(answers.keys()) >= 15:
  #             break
  #           if index%1000 == 0:
  #             print(f"tried: {index}times\nenumerating: {sometry}\nanswers so far: {len(answers.keys())}")
  # timetaken = time.time()-start

  # print(f"total time taken: {timetaken}")
  # print(f"exhausted dict time taken: {exhausted_dict_time}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", default="3.txt", help="input file to read for hash values")
  parser.add_argument("-w", "--with_dict", default="words5.txt", help="with help using dictionary")
  parser.add_argument("-o", "--output", default="output.txt", help="output a file with key=value")
  args=parser.parse_args()
  run()