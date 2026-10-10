from calculator import add

def test_add_numbers():
    # בדיקה שהפונקציה מחזירה 5 עבור 2 ו-3
    assert add(2, 3) == 5

def test_add_negative_numbers():
    # בדיקה שהפונקציה עובדת גם עם מספרים שליליים
    assert add(-1, 1) == 0
