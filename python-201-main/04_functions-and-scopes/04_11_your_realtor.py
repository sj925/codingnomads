# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def advert(**kwargs: str) -> list[str]:
    """takes in key/value args and returns a list of the information"""
    print("Real Estate advertisement information:\n")
    details_list = [f"{k.capitalize()}: {v}" for k,v in kwargs.items()]
    details = ("\n".join(details_list))
    return details

print(advert(
    home="a wonderful 4bd 3bath two story home",
    price="$500,000",
    agent="Sean Burke",
    contact="555-555-0000"))