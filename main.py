from termcolor import colored

# nums = [all the numbers]
# target = sum of two nums indies
# only one solution
# same element cannot be used twice
# return answer in any order

# code has to check if 2 indices in list add to target and return the 2 indices.

def twoSum(nums, target):
    for i in range(len(nums)):
        # print("---")
        # print(colored((nums[i]), "red"))

        for j in range(len(nums)):
            while (j + 1) < len(nums) and i != (j + 1):
                # print(colored(nums[j + 1],"blue"))
                # print("-----")
                # print(colored(nums[i] + (nums[j + 1]), "magenta"))
                if nums[i] + (nums[j + 1]) == target:
                    # print(colored((i, (j+1)), "green"))  # ANSWER IS HERE
                    the_answer = []
                    the_answer.append(i)
                    the_answer.append(j + 1)
                    return the_answer

                # print("-----")
                break




nums = [3,3]
target = 6

print(colored(twoSum(nums, target), "green"))