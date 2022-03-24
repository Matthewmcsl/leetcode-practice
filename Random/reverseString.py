# Reverse a string without slicing it!
# e.g., Reverse the string: 'nwod uoy tel annog reven, pu uoy evig annog reven'


def reverse(s: str) -> str:

    store = []
    for letter in s:
        store.append(letter)

    l_point, r_point = 0, len(store) - 1

    while l_point < r_point:
        store[l_point], store[r_point] = store[r_point], store[l_point]
        l_point += 1
        r_point -= 1

    return "".join(store)


print(reverse("nwod uoy tel annog reven, pu uoy evig annog reven"))

# similarly, we can slice the string like this

rick_roll = "nwod uoy tel annog reven, pu uoy evig annog reven"
print(rick_roll[::-1])
