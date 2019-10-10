#!/usr/bin/python

import sys

def multiplier(cache):
  base_cache = [['rock'], ['paper'], ['scissors']]
  emt_cache = []
  for i in cache:
    for j in range(len(base_cache)):
      n = i + base_cache[j]
      emt_cache.append(n)
      
  return emt_cache

def rock_paper_scissors(n, cache=None):
  if n == 0:
    if not cache:
      cache = [[]]
    return cache
  
  if n == 1:
    if not cache:
      cache = [['rock'], ['paper'], ['scissors']]
      return cache
    cache = multiplier(cache)
    cache = rock_paper_scissors(n-1, cache)
    return cache
  
  
  else:
    if not cache:
      cache = [['rock'], ['paper'], ['scissors']]
      n -= 1
    cache = multiplier(cache)
    
    cache = rock_paper_scissors(n-1, cache)
    
    return cache


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')