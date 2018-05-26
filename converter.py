from zeep import Client


def convert_temp(avg_temp):
    client = Client("https://www.w3schools.com/xml/tempconvert.asmx?WSDL")
    return client.service.FahrenheitToCelsius(avg_temp)


def convert_curr(data):
    client = Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    return client.service.ConvertToNum(fromCurrency=data[2], toCurrency="rub", amount=data[1], rounding="1")


def avg_temp():
    with open("temps.txt", "r") as f:
        temps = [int(line.split()[0]) for line in f]
        avg_temp = sum(temps) / len(temps)
        result = float(convert_temp(avg_temp))
        print("Средняя температура: {} С".format(round(result)))


def travel_cost():
    with open("currencies.txt", "r") as f:
        total_result = int()
        for line in f:
            data = line.split()
            convert_result = convert_curr(data)
            total_result += convert_result
    print("Стоимость путешествия: {} руб.".format(round(total_result)))


if __name__ == "__main__":
    travel_cost()
    avg_temp()
