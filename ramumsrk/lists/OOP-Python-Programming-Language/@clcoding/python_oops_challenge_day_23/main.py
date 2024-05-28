#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging confiuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent}/logs/python_oops_challenge_day_23.log'
)

import Sunglasses.sunglasses

from Sunglasses.sunglasses import Sunglasses

if __name__ == '__main__':

  first_instance: Sunglasses = Sunglasses()
  logging.debug(f'{first_instance=}')
  logging.debug(
    F'{first_instance.print_shade_index()=}'
  )