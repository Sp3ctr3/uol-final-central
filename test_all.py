from recognition import run_recognition

def test_check_if_same_image_recognized():
    results = run_recognition("test_files/yashin2.jpg")
    assert results[0]==True

def test_check_if_correct_person_recognized():
    results = run_recognition("test_files/yashin1.jpg")
    assert results[0]==True

def test_check_if_wrong_person_recognized():
    results = run_recognition("test_files/cash.jpg")
    assert results[0]==False

def test_check_if_wrong_object_recognized():
    results = run_recognition("test_files/cow.jpg")
    assert results[0]=="No faces found!"

