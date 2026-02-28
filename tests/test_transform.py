from utils.transform import transform


def test_transform_empty_data():
    result = transform([])
    assert result.empty


def test_transform_remove_unknown():
    data = [{
        "Title": "Unknown Product",
        "Price": "$10",
        "Rating": "4.5 / 5",
        "Colors": "3 Colors",
        "Size": "Size: M",
        "Gender": "Gender: Men"
    }]
    result = transform(data)
    assert result.empty


def test_transform_invalid_price():
    data = [{
        "Title": "Test Shirt",
        "Price": "INVALID",
        "Rating": "4.5 / 5",
        "Colors": "3 Colors",
        "Size": "Size: M",
        "Gender": "Gender: Men"
    }]
    result = transform(data)
    assert result.empty


def test_transform_valid_data():
    data = [{
        "Title": "Test Shirt",
        "Price": "$10",
        "Rating": "4.5 / 5",
        "Colors": "3 Colors",
        "Size": "Size: M",
        "Gender": "Gender: Men"
    }]

    result = transform(data)

    assert not result.empty
    assert result.iloc[0]["Price"] == 160000.0   # float
    assert result.iloc[0]["Rating"] == 4.5
    assert result.iloc[0]["Colors"] == 3
    assert result.iloc[0]["Size"] == "M"
    assert result.iloc[0]["Gender"] == "Men"