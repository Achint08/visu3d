# Copyright 2022 The visu3d Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for py_utils."""

from __future__ import annotations

from visu3d.utils import py_utils


def test_group_by():
  out = py_utils.groupby(
      [0, 30, 2, 4, 2, 20, 3],
      key=lambda x: x < 10,
  )
  # Order is consistent with above
  assert out == {
      True: [0, 2, 4, 2, 3],
      False: [30, 20],
  }


def test_group_by_value():
  out = py_utils.groupby(
      ['111', '1', '11', '11', '4', '555'],
      key=len,
      value=int,
  )
  # Order is consistent with above
  assert out == {
      1: [1, 4],
      2: [11, 11],
      3: [111, 555],
  }
