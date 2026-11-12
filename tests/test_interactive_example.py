
import subprocess
import sys


def test_interactive_birth_date():
    result = subprocess.run(
        [
            sys.executable,
            "examples/step_04_interactive_birth_date.py",
        ],
        input="31.02.1986\n04.05.1986\n",
        text=True,
        capture_output=True,
        check=True,
        timeout=10,
    )

    assert "Попробуйте ещё раз." in result.stdout
    assert "Дата рождения: 04.05.1986" in result.stdout
    assert "центр=3" in result.stdout
