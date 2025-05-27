def convert_currency(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'RUB': 75.0
    }

    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be numeric")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if from_currency not in rates or to_currency not in rates:
        raise KeyError("Unsupported currency")

    in_usd = amount / rates[from_currency]
    converted_amount = in_usd * rates[to_currency]
    return round(converted_amount, 2)