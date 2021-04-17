# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-


#########################################################################################
def isrootfolder_test():
    from utilmy import (os_path_isrootfolder)

    #####################################################################################
    assert os_path_isrootfolder("/"), "'/': it's not root folder"
    assert os_path_isrootfolder("/./"),  "'/./': it's not root folder"
    assert os_path_isrootfolder("/././"),  "'/././': it's not root folder"
    assert os_path_isrootfolder("/.."), "'/..': it's not root folder"
    assert os_path_isrootfolder("/../.."), "'/..': it's not root folder"

    assert not os_path_isrootfolder(), "'': it's root folder"
    assert not os_path_isrootfolder("../utilmy"), "'../utilmy': it's root folder"

def every_test():
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

def timeago_test():
    import datetime
    from utilmy import (timeago)

    #####################################################################################
    right_now = datetime.datetime.now()
    assert timeago(right_now + datetime.timedelta(seconds=5), right_now) == None
    assert timeago(right_now, right_now) == 'less than 1 second ago'
    assert timeago(right_now - datetime.timedelta(seconds=1), right_now) == 'about 1 second ago'
    assert timeago(right_now - datetime.timedelta(seconds=59), right_now) == 'about 59 seconds ago'
    assert timeago(right_now - datetime.timedelta(seconds=60), right_now) == 'about 1 minute ago'
    assert timeago(right_now - datetime.timedelta(minutes=1), right_now) == 'about 1 minute ago'
    assert timeago(right_now - datetime.timedelta(minutes=59), right_now) == 'about 59 minutes ago'
    assert timeago(right_now - datetime.timedelta(minutes=60), right_now) == 'about 1 hour ago'
    assert timeago(right_now - datetime.timedelta(hours=1), right_now) == 'about 1 hour ago'
    assert timeago(right_now - datetime.timedelta(hours=23), right_now) == 'about 23 hours ago'
    assert timeago(right_now - datetime.timedelta(hours=24), right_now) == 'about 1 day ago'
    assert timeago(right_now - datetime.timedelta(days=1), right_now) == 'about 1 day ago'
    assert timeago(right_now - datetime.timedelta(days=29), right_now) == 'about 29 days ago'
    assert timeago(right_now - datetime.timedelta(days=30), right_now) == 'about 1 month ago'
    assert timeago(right_now - datetime.timedelta(days=59), right_now) == 'about 1 month ago'
    assert timeago(right_now - datetime.timedelta(days=60), right_now) == 'about 2 months ago'
    assert timeago(right_now - datetime.timedelta(days=89), right_now) == 'about 2 months ago'
    assert timeago(right_now - datetime.timedelta(days=90), right_now) == 'about 3 months ago'
    assert timeago(right_now - datetime.timedelta(days=365), right_now) == 'about 1 year ago'
    assert timeago(right_now - datetime.timedelta(days=750), right_now) == 'about 2 years ago'

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
