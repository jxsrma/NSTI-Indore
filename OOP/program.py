from States import State, Person

mp = State("Madhya Pradesh", "Bhopal", 100000000, ["Omkareshwar", "Mahakaleshwar",
                                                   "Rajwada", "Bheda Ghat", "Gwalior Fort"], ["Poha Jalebi", "Daal Bafle", "Namkeen"])

rj = State("Rajasthan",
           "Jaipur",
           123123918471,
           ["Jaighad", "Hawamahal", "Chittodh Fort",
            "Randhambhor Fort", "Khatu Shyam Ji", "Shambhar Jheel", "Mount Abu"], ["Daal Bati Churma", "Besan Gatta", "Amrood", "Moog Bade"])

# mp.printDetails()
# rj.printDetails()


shyam = Person("Shyam", 45, rj.capital)
# shyam.address = rj.capital
shyam.printDetails()

# print(type(Person()))
# print(type(shyam))
# print(type(int()))

# print(State.Country)
# print(State.name)
