#!/usr/bin/python

import argparse

def find_max_profit(prices):
    d = dict(enumerate(prices))
    l = len(d)

    profit_lst = []
    count = 1
    
    for i in d:  
        for i in range(count, l):
            num = (d[count] - d[i])*-1
            profit_lst.append(num)
        count +=1
        
    for i in profit_lst:
        if i == 0:
            profit_lst.remove(i)
        
    return max(profit_lst)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))