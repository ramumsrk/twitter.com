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
  filename=f'{Path(__file__).parent}/logs/float_as_an_argument_to_builtin_range_function.log'
)

import Range.builtin_range_function_demo

if __name__ == '__main__':

  sample_input_number: Literal[float] = float( input( 'Enter a number: ') )

  # Function call
  Range.builtin_range_function_demo.builtin_range_function_demo(sample_input_number)