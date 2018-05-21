import os
from zeep import Client


def convert_temp(avg_temp):
    client = Client("https://www.w3schools.com/xml/tempconvert.asmx?WSDL")
    return client.service.FahrenheitToCelsius(avg_temp)


def convert_curr(data):
    client = Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    return client.service.ConvertToNum(fromCurrency=data[2], toCurrency="rub", amount=data[1], rounding="1")


def get_avg_temp(file):
    with open(file, "r") as f:
        temps = [int(line.split()[0]) for line in f]
        avg_temp = sum(temps) / len(temps)
        result = float(convert_temp(avg_temp))
        print("Средняя температура: {} С".format(round(result)))


def get_travel_cost(file):
    with open(file, "r") as f:
        total_result = int()
        for line in f:
            data = line.split()
            convert_result = convert_curr(data)
            total_result += convert_result
    print("Стоимость путешествия: {} руб.".format(round(total_result)))


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    while True:
        inp = input("\n1 - Средняя температура\n2 - Стоимость путешествия\n0 - Закончить\nВведите занчение 1, 2 или 0: ")
        if inp == "1":
            get_avg_temp(os.path.join(directory, "temps.txt"))
        elif inp == "2":
            get_travel_cost(os.path.join(directory, "currencies.txt"))
        elif inp == "0":
            break
main()