#! /usr/bin/python3.12

from break_continue_and_list import numbers, some_numbers

from typing import Literal

import logging

# User-defined function
def main() -> Literal[None]:
  for number in numbers:
    if number % 2 == 0:
      continue
    some_numbers.append(number)
    break
  return None

if __name__ == '__main__':

  logging.debug(
    f'{main()=}'
  )
  logging.debug(
    F'{numbers=}'
  )
  logging.debug(
    f'{some_numbers=}'
  )