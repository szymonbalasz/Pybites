import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    "arg, expected", [
        ("cardio", "Wed\n"),
        ("lower", "Tue, Fri\n"),
        ("upper", "Mon, Thu\n"),
        ("abs", "No matching workout\n"),
        ("hrs", "No matching workout\n")

    ])
def test_print_workout_days(capsys, arg, expected):
    print_workout_days(arg)
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ''
