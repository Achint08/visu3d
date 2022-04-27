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

"""Tests for auto_plot."""

from unittest import mock

import visu3d as v3d


def test_auto_plot():
  with mock.patch('IPython.get_ipython', mock.MagicMock()) as ipython_mock:
    v3d.auto_plot_figs()
  assert ipython_mock.call_count == 1