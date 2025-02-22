# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
fmt:
	hatch fmt

test:
	hatch test

test_pytest:
	PYTHONPATH="$(shell pwd)/src" pytest
