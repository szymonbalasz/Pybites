from unittest.mock import patch

import pytest

import color

#########

hex_colors = [
    (0, 0, 0, '#000000'),
    (255, 0, 0, '#FF0000'),
    (0, 0, 200, '#0000C8')
]


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@pytest.mark.parametrize('r, g, b, expected', hex_colors)
@patch('color.sample')
def test_gen_hex_color(mock_obj, gen, r, g, b, expected):
    mock_obj.return_value = r, g, b
    assert next(gen) == expected
    mock_obj.assert_called_with(range(0, 256), 3)
