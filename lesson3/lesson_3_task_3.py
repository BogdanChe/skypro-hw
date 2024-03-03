from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Примерная улица", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Тестовая улица", "20", "15")

mailing = Mailing(to_address, from_address, 500, "ABC123")

print(f"Отправление {mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mailing.cost} рублей.")
