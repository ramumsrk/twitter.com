#! /usr/bin/python3.12

from typing import Literal

# User-defined function
def main() -> Literal[None]:
  d: Literal[int] = 0
  a = b = c = d
  assert a == 0 and b == 0 and c == 0 and d == 0
  print(
    'a = {a}\nb = {b}\nc = {c}\nd = {d}'.format(
      a=a,
      b=b,
      c=c,
      d=d
    )
  )
  return None

if __name__ == '__main__':

  print(
    f'{__name__=}'
  )

  # Function call
  main()