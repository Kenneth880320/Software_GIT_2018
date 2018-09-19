
from fuzzing.fuzzer import FuzzExecutor

number_of_runs = 13

def test():
    fuzz_executer = FuzzExecutor(["python rle.py -d".replace(" ", "&")],["FuzzTest.txt"])
    fuzz_executer.run_test(number_of_runs)
    print("test Finished!")
    return fuzz_executer.stats


def main():
    print("Test is running!")
    stats = test()
    print(stats)

if __name__ == "__main__":
    main()
