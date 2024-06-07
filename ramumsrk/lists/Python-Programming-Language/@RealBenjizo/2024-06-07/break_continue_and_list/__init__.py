#! /usr/bin/python3.12

from typing import List

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%B, %A %d, %Y %H:%M:%S %Z %z",
  filemode='+at',
  filename=F'{Path(__file__).parent.parent}/logs/break_continue_and_list.log'
)

logging.debug(
  f'{__name__=}'
)
logging.debug(
  F'{type(logging)=}'
)
logging.debug(
  f'{logging.__name__=}'
)
logging.debug(
  F'{logging.__path__=}'
)
logging.debug(
  f'{logging.__file__=}'
)

numbers: List[int] = [
  1,
  2,
  3,
  4,
  5,
]

some_numbers: List[int] = []