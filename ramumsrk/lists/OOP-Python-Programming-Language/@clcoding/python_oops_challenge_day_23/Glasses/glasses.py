#! /usr/bin/python3.12

from typing import Self, Literal

class Glasses:
  # Instance creation
  def __new__(
    klass,
    *args,
    **kwargs
  ) -> Self:
    return super().__new__(klass)
  # Instance initialization
  def __init__(
    self,
    /
  ) -> Literal[None]:
    return None