def poisk(A, B):
    lst = [1, 2, 3, 4, 6, 12, 23, 55, 66, 235, 235235, 456, 54, 77,23, 345, 675,89,867,345,1, 234,456,7645,123,654, 3645, 346, 365]
    lst_index = []
    for i in range (len(lst)):
        if lst[i]> A and lst[i]<B :
            lst_index.append(i)

    print("перечень индексов элементов входящих в диапазон :", lst_index)

A = int(input("введите Нижний диапазон поиска : "))
B = int(input("введите Верхний диапазон поиска : "))
poisk(A, B)