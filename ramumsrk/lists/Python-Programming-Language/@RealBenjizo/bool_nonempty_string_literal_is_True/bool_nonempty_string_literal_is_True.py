#! /usr/bin/python3.12

from typing import Literal

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/logs/bool_nonempty_string_literal_is_True.log'
)

# User-defined function
def greet(sample_input_name: str) -> Literal[None]:
  logging.debug(
    f'Hello, {sample_input_name}!'
  )
  return None

if __name__ == '__main__':

  logging.debug(
    F"{(bool('')==False)=}"
  )

  logging.debug(
    f'{bool("Alice")=}'
  )

  if "Alice" != True:
    # Function call
    logging.debug(
      F"{greet('Bob')=}"
    )