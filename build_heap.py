def build_heap(numbers):
    swaps = []

    for i in reversed(range(len(numbers))):
        j = i
        while j > 0 and numbers[(j-1)//2] > numbers[j]:
            parent = (j-1)//2
            swaps.append((parent, j))
            numbers[j], numbers[parent] = numbers[parent], numbers[j]
            j = parent

    return swaps



def main():
    
    input_type = input("")
    if "I" in input_type:
        n = int(input())
        assert 1 <= n <= 100000
        numbers = []
        for i in range(n):
            num = int(input().replace("\\r\\n",""))
            assert 0 <= num <= 109
            numbers.append(num)
    else:
        file_path = input("")
        with open(f"./tests/{file_path}", "r") as file:
            n = int(file.readline())
            assert 1 <= n <= 100000
            numbers = []
            for i in range(n):
                num = int(file.readline())
                assert 0 <= num <= 109
                numbers.append(num)

    assert len(numbers) == n

    swaps = build_heap(numbers)

    print(len(swaps))
    for i, j in swaps:
    	print(i, j)


if __name__ == "__main__":
    main()
