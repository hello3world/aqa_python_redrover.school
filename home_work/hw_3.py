def task_1():
    list1 = [i for i in range(101) if i % 2 == 0 and i % 3 == 0]
    print(list1)


def task_2():
    items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
    numbers = [i for i in items if isinstance(i, (float, int))]
    s = sum(numbers)
    print(s)


def task3():
    list1 = []
    while True:
        message = input("type message: ").casefold()
        if message == "by":
            print("By By")
            print(list1)
            break
        list1.append(message)
        if len(list1) > 4:
            list1.pop(0)


task3()

task_2()

task_1()
