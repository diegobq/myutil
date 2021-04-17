# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-


#########################################################################################
def test1():
    from utilmy import (os_path_isrootfolder)

    #####################################################################################
    assert os_path_isrootfolder("/"), "'/': it's not root folder"
    assert os_path_isrootfolder("/./"),  "'/./': it's not root folder"
    assert os_path_isrootfolder("/././"),  "'/././': it's not root folder"
    assert os_path_isrootfolder("/.."), "'/..': it's not root folder"
    assert os_path_isrootfolder("/../.."), "'/..': it's not root folder"

    assert not os_path_isrootfolder(), "'': it's root folder"
    assert not os_path_isrootfolder("../utilmy"), "'../utilmy': it's root folder"

def test2():
    from utilmy import (every)

    #####################################################################################
    assert every(), 'Not every TRUE'
    assert every([]), 'Not every TRUE'
    assert every([1,2,3,4,5]), 'Not every TRUE'
    assert every([True, True, True]), 'Not every TRUE'
    assert every([2, 4, 6], lambda x, y, z: (x % 2) == 0), 'Not every TRUE'
    assert every([1, 5, 15], lambda x, y, z: (x % 2) != 0), 'Not every TRUE'
    assert every([1, 5, 15], lambda x, index, z: index < 3), 'Not every TRUE'
    assert every([1, 5, 15], lambda x, index, items: items[index] < 16), 'Not every TRUE'

    assert not every([0, 0, 0]), 'every TRUE'
    assert not every([True, False, True]), 'every TRUE'
    assert not every([1, 5, 15], lambda x, index, items: items[index] < 15), 'every TRUE'

if __name__ == "__main__":
    import utilmy_test
    tests = list(filter(lambda functionName: not functionName.startswith("__"), dir(utilmy_test)))
    testsTotal = len(tests)
    testsCounter = 0
    try:
        for testName in tests:
            getattr(utilmy_test, testName)()
            print(f"{testName}: OK")
            testsCounter += 1
    except Exception as e :
        print( f"{e}")
    print(f"{testsCounter}/{testsTotal}")
