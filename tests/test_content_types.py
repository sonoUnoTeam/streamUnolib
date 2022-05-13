import pytest

from streamunolib import content_type
from streamunolib.content_types import ContentType


@pytest.mark.parametrize(
    'mimetype, expected',
    [
        ('jpg', 'image/jpeg'),
        ('wav', 'audio/wav'),
        ('audio/mpeg', 'audio/mpeg'),
    ],
)
def test_content_types(mimetype: str, expected: str) -> None:
    actual = content_type(mimetype)
    assert actual == ContentType(expected)
