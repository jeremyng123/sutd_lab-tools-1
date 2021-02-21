# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:44:12 2021

@author: Joshua ft. Jeremy Ng

* This file is based on Jem's  split_hash.py
* takes in the hash and pw txt file that is output by hashcat
* with each line in the format <hash>:<pw>
* outputs competition.csv with 2 col: hash and password
* by default it uses a testing file i used called 'weakout.txt'
"""
import pandas as pd
import argparse

def txtToCsv(file):
    
    #I thought we had to name separate files at first, guess it's boring old 'competition.csv'
    #filename = file.split('.')[0]
    
    dlmt = ": \n\r\t"
    
    decoded = open(file,'r')
    diCoded = {'hash':[], 'password':[]}
    
    for line in decoded:
        words = line.strip(dlmt).split(':')
        if len(words) == 2:
            diCoded['hash'].append(words[0])
            diCoded['password'].append(words[-1])
    decoded.close()
    
    output = pd.DataFrame(diCoded)
    
    #output.to_csv(filename + '.csv', index=None)
    output.to_csv('competition.csv', index=None)


#learn this best practice from jem korkor
if (__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", 
                        default="weakout.txt", 
                        help="input file to read for hash and pw pairs")
    args=parser.parse_args()
    txtToCsv(args.input)