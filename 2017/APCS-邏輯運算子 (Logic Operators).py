nums = list(map(int, input().split()))
nums = list(map(bool, nums))

flag = True
if nums[0] & nums[1] == nums[2]:
    print("AND")
    flag = False

if nums[0] | nums[1] == nums[2]:
    print("OR")
    flag = False
    
if nums[0] ^ nums[1] == nums[2]:
    print("XOR")
    flag = False
    
if flag:
    print("IMPOSSIBLE")