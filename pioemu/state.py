# Copyright 2021, 2022 Nathan Young
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections import deque
from dataclasses import dataclass, field

from .shift_register import ShiftRegister


def ShiftRegisterFactoryMin():
    return ShiftRegister(0, 0)


def ShiftRegisterFactoryMax():
    return ShiftRegister(0, 32)


@dataclass(frozen=True)
class State:
    clock = 0
    program_counter = 0
    pin_directions = 0
    pin_values = 0
    transmit_fifo = field(default_factory=lambda: deque())
    input_shift_register = field(default_factory=ShiftRegisterFactoryMin)
    output_shift_register = field(
        default_factory=ShiftRegisterFactoryMax
    )
    x_register = 0
    y_register = 0
