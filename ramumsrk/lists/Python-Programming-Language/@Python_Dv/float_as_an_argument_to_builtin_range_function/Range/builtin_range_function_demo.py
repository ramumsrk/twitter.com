#! /usr/bin/python3.12

from typing import Literal

import logging

# User-defined function
def builtin_range_function_demo(
  sample_input_number: Literal[float],
  /
) -> Literal[None]:
  try:
    for sample_number in range(sample_input_number):
      logging.debug(
        f'Sample number is: {sample_number}'
      )
  except ValueError as valueError:
    logging.error(
      F'{valueError}'
    )
  except TypeError as typeError:
    logging.error(
      f'{typeError}'
    )
  except Exception as exception:
    logging.error(
      F'{exception}'
    )
  return None