import pytest

from streamunolib import content_type


@pytest.mark.parametrize(
    'mimetype, expected',
    [
        ('jpg', 'image/jpeg'),
        ('wav', 'audio/x-wav'),
    ],
)
def test_content_types(mimetype: str, expected: str) -> None:
    actual = content_type(mimetype)
    assert actual['content_type'] == expected
