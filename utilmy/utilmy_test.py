# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-


#########################################################################################
def test1():
    from utilmy import (os_isRootFolder)

    #####################################################################################
    assert os_isRootFolder("/"), "'/': it's not root folder"
    assert os_isRootFolder("/./"),  "'/./': it's not root folder"
    assert os_isRootFolder("/././"),  "'/././': it's not root folder"
    assert os_isRootFolder("/.."), "'/..': it's not root folder"
    assert os_isRootFolder("/../.."), "'/..': it's not root folder"

    assert not os_isRootFolder(), "'': it's root folder"
    assert not os_isRootFolder("../utilmy"), "'../utilmy': it's root folder"

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
