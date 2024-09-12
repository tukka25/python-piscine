ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World"
ft_dict["Hello"] = "42AbuDhabi"
tmp_list = ["Hello", "Uae"]
ft_tuple = tuple(tmp_list)
ft_set.remove("tutu!")
ft_set.add("AbuDhabi")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# list is changeable "nutable"
# tuple not changeable "immutable"
# set like list but it u cant change or index and no duplicates.
# dictinory key value pairs no dublicate key