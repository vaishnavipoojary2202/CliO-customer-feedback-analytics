from src.data_preprocessing import is_candidate_smartphone


def test_iphone_is_candidate():
    assert is_candidate_smartphone("Apple iPhone 15 Pro 128GB")


def test_pixel_is_candidate():
    assert is_candidate_smartphone("Google Pixel 8 smartphone")


def test_case_is_excluded():
    assert not is_candidate_smartphone("Protective case for iPhone 15")


def test_charger_is_excluded():
    assert not is_candidate_smartphone("Fast charger for mobile phone")


def test_empty_title_is_not_candidate():
    assert not is_candidate_smartphone("")
    assert not is_candidate_smartphone(None)
