def getRanges(nums):
    n = len(nums)
    i, j = 0, 1
    ans = ""

    while j < n:
        if nums[j] == nums[j - 1] + 1:
            j += 1
        else:
            if j - i == 1:
                ans += f"{nums[i]}, "
            elif j - i > 1:
                ans += f"{nums[i]}->{nums[j - 1]}, "
            i = j
            j += 1

    if j - i == 1:
        ans += f"{nums[i]}, "
    elif j - i > 1:
        ans += f"{nums[i]}->{nums[j - 1]}, "

    return ans[:-2]


input_list = input()
if input_list == "":
    print("No numbers provided")
else:
    lst = []
    try:
        lst = list(map(int, input_list.split()))
        print(getRanges(lst))
    except ValueError:
        print("All elements must be integers")
