def plotAreaAmountCalculation(length: float, breadth: float, rate: float):
    """This function calculates total amount of property by giving Length, Breadth and Rate per square meter"""
    amount = length*breadth*rate
    return amount

# Hello


def rateCalculation(l, b, amount):
    """This function calculates the rate of property by giving Length, Breadth and Amount of the Property"""
    rate = amount/(l*b)
    return rate