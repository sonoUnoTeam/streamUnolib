import pytest

from streamunolib import media_type


@pytest.mark.parametrize(
    'mimetype, expected',
    [
        ('jpg', 'image/jpeg'),
        ('wav', 'audio/x-wav'),
    ],
)
def test_media_type_ext(mimetype: str, expected: str) -> None:
    actual = media_type(mimetype)
    assert actual['contentMediaType'] == expected
    assert 'x-contentMediaEncoding' not in expected


@pytest.mark.parametrize('generic_type_name', ['audio', 'image', 'video'])
def test_media_type_generic(generic_type_name: str) -> None:
    actual = media_type(generic_type_name, info=None)
    assert actual['contentMediaType'] == generic_type_name + '/*'
    assert 'x-contentMediaEncoding' in actual
    assert actual['x-contentMediaEncoding'] == {'info': None}


def test_media_type_unknown_error() -> None:
    with pytest.raises(ValueError, match='No MIME type known for extension'):
        media_type('unknown file extension')


def test_media_type_non_generic_error() -> None:
    with pytest.raises(TypeError, match='should only be specified for generic'):
        media_type('wav', info=None)
