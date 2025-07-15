from address import Address

from mailing import Mailing

to_address = Address("195298", "Санкт-Петербург", "Косыгина", "34", "125")
from_address = Address("245354", "Калининград", "Маяковского", "15", "7")
track = "TRK347995"
cost = 270

mailing = Mailing(to_address, from_address, cost, track)
print(f"Отправление {mailing.track} из {mailing.from_address}"
      f" в {mailing.to_address}. Стоимость {mailing.cost} рублей.")
