# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:07:30 2014

@author: datumZ
"""

from numpy import *
import collections

#mapping dict                       
con_d = {i:str(i+i//9) if len(str(i+i//9)) == 2 else '0'+str(i+i//9) for i in range(81)}  
rev_d = dict(zip(con_d.values(),con_d.keys()))
#initialize symbol set for checking
s = set(range(1,10))
rec = collections.OrderedDict()

#initialize sudoku board
def initialize_board():
    b = zeros((9,9))
    #define one row at a time, enter 0 for blank
    for r in range(9):
        user_i = input("enter row #{}. No spaces or commas, zero for blank:".format(r))
        b[r,:] = [int(user_i[i]) for i in range(9)]
        #TODO input validation
    return b

#initialize test board
def init_test_board():
    b = zeros((9,9))
    b[0,:] = [0,0,4,0,9,0,1,6,0]
    b[1,:] = [0,0,1,3,7,0,9,0,8]
    b[2,:] = [0,0,0,0,0,2,0,4,3]
    b[3,:] = [0,8,0,0,0,1,0,0,0]
    b[4,:] = [4,0,0,0,2,0,0,0,0]
    b[5,:] = [3,2,0,0,0,0,0,7,0]
    b[6,:] = [0,5,0,2,4,0,3,0,0]
    b[7,:] = [0,0,3,7,5,8,2,0,0]
    b[8,:] = [8,0,2,1,0,3,0,0,9]
    return b
    
b = init_test_board()        
#TODO set global b, classify module
#define checker function
def check(b):
    #iterate over rows
    for r in range(9):
        if set(b[r,:]) != s:
            print("row {} false".format(r))
            return False
    #iterate over columns
    for c in range(9):
        if set(b[:,c]) != s:
            print("column {} false".format(c))
            return False
    #iterate over squares
    coords = [(0,3),(3,6),(6,9)]
    for (y1,y2) in coords:
        for (x1,x2) in coords:
            sq = b[y1:y2,x1:x2].tolist()
            sq = set([item for sublist in sq for item in sublist])
            if sq != s:
                print("box {}:{},{}:{} false".format(y1,y2,x1,x2))
                return False
    print("congratulations!")
    return True

def get_coors(k):
    return int(k[0]), int(k[1])
        
#generate candidates for a box
def cands(k,b):
    r,c = get_coors(k)
    row = set(b[r,:].tolist())
    col = set(b[:,c].tolist())
    coords = [(0,3),(3,6),(6,9)]
    d = dict()
    for (i,j) in coords:
        if r in range(i,j): d['rs'] = (i,j)
        if c in range(i,j): d['cs'] = (i,j)
    sq = b[d['rs'][0]:d['rs'][1],d['cs'][0]:d['cs'][1]].tolist()
    sq = set([item for sublist in sq for item in sublist])
    return s - (row.union(col,sq))
 
#brute force solution finder
def brute_sudoku(b):
    start = 0
    skip_rec = False
    global rec
    while start < 81:
        print(b)
        k = con_d[start]
        r,c = get_coors(k)
        if len(cands(k,b)) > 0 and (b[r,c] == 0 or skip_rec == True):
            if skip_rec == False: rec[k] = cands(k,b)
            else: skip_rec=False
            try: b[r,c] = next(iter(rec[k]))
            except KeyError: pass 
            start += 1
        elif b[r,c] != 0:
            start += 1
        else:
            print('backtracking')
            while True:
                lastK = next(reversed(rec))
                r,c = get_coors(lastK)
                wrong_guess = b[r,c]
                rec[lastK] -= {wrong_guess}
                if len(rec[lastK]) > 0:
                    start = rev_d[lastK]
                    skip_rec = True
                    break
                else:
                    rec.pop(lastK)
                    b[r,c] = 0
    print(b)
    return b

sol = brute_sudoku(b)

#This line is a test of my git skills
                        
                        
                        
                        
                        
                        
                        