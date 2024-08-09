from address import Address
from mailing import Mailing

letter = Mailing(Address("452837", "Уфа", "Центральная", "22", "45"), 
                 Address("452833",  "Москва", "Ленина", "4", "55"), 
                 "$825.78", "87654322")

print(f"Letter with the tracking number {letter.track} mailed from address: {letter.from_address} to: {letter.to_address}. Cost of mailing: {letter.cost}")