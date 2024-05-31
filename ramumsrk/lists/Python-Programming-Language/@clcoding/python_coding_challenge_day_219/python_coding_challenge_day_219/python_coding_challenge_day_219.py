#! /usr/bin/python3.12

from typing import Literal

# User-defined function
def foo(
  a: Literal[int],
  b: Literal[int] = 5,
  c: Literal[int] = 10
) -> Literal[int]:
  return a + b + c