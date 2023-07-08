from twttr import shorten

def test_lower_upper_vow():
    assert shorten('twitter') == 'twttr'
    assert shorten('asdasdasd') == 'sdsdsd'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_numbers():
    assert shorten('1234ab') == '1234b'

def test_specials():
    assert shorten('aaa!1@2') == '!1@2'
