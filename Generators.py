def csv_reader(filename):
    with open(filename, "r") as file:
        for row in file:
            yield row.strip()


if __name__ == '__main__':
    csv_gen = (line.strip() for line in open("./techcrunch.csv"))

    print(type(csv_gen))

    # it = iter(csv_gen)

    for i in range(10):
        print(f"{i} : {next(csv_gen)}")

    # for line in csv_gen:
    #     print(line)

    # for i, line in enumerate(csv_reader("job_train.csv")):
    #     print(i, line)
    #     # prints 1st 10 lines
    #     if i == 9:
    #         break
    #
    # csv_lines = list(csv_reader("job_train.csv"))
    #
    # print(type(csv_lines))

    square_gen = (i*i for i in range(5))
    print(next(square_gen))
    print(next(square_gen))
    print(next(square_gen))
    print(next(square_gen))
    print(next(square_gen))
