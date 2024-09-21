score = int(input())

match score:
    case _ if 90 <= score <= 100:
        print("A")
    case _ if 80 <= score < 90:
        print("B")
    case _ if 70 <= score < 80:
        print("C")
    case _ if 60 <= score < 70:
        print("D")
    case _:
        print("F")
