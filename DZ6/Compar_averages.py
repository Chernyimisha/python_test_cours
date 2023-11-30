class Compar_averages:
    @staticmethod
    def compare_averages(list1_average, list2_average):
        if list1_average > list2_average:
            print("Первый список имеет большее среднее значение")
        elif list1_average < list2_average:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
