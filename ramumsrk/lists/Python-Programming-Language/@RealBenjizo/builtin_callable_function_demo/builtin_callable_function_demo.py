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
  filename=F'{Path(__file__).parent}/logs/builtin_callable_function_demo.log'
)

# User-defined function
def greet(sample_input_string: Literal[str]) -> Literal[None]:
  logging.debug(
    F'Hello, {sample_input_string}'
  )
  return None

if __name__ == '__main__':

  sample_input_string: Literal[str] = 'Hello, how are you?'

  logging.debug(
    f'{greet(sample_input_string)=}'
  )

  logging.debug(
    F'{callable(sample_input_string)=}'
  )
  # `greet' indicates
  # a reference to the
  # user-defined function
  # greet()
  # `greet()' indicates a
  # function call
  logging.debug(
    f'{callable(greet)=}'
  )