import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError) as error:
        encrypt_message("Hello world!", "little potato")
    assert str(error.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as error:
        encrypt_message(2024, 2)
    assert str(error.value) == "tipo inválido para message"

    assert encrypt_message("XFAIL", 99) == "LIAFX"

    assert encrypt_message("XFAIL", 3) == "AFX_LI"

    assert encrypt_message("XFAIL", 4) == "L_IAFX"
