from polimorf import Polimorf


def main():
    file_name = 'var1.csv'
    p = Polimorf(file_name)
    ~p
    p.split_data()

if __name__ == "__main__":
    main()
