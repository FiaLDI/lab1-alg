

if __name__ == '__main__':
    count = 0
    maximum = 0
    with open("17.txt") as numbers:
        nums = [int(i) for i in numbers]
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] * nums[j] % 26 == 0:
                    count += 1
                    maximum = max(maximum, nums[i] + nums[j])
    print(count, maximum)