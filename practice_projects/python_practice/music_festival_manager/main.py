from enum import Enum, IntEnum
import enums as e
import cls_artist as ca
import cls_slot as cs
import cls_festival as cf


Deftones = ca.Artist("Deftones", 666, e.Genre.ROCK, e.StageSize.MAINSTAGE)
print(Deftones)

artist_slot1 = cs.Slot(1, Deftones, e.StageSize.MEDIUM, "Saturday", "17:00")
print(artist_slot1)

if __name__ == "__main__":
# ── Build the festival ────────────────────────────────────────
    festival = cf.Festival("Lowlands 2026")
    #office   = TicketOffice()

    print("\n── Adding Artists ──")
    festival.add_artist(ca.Artist("Bicep",           1, e.Genre.ELECTRONIC, e.StageSize.LARGE))
    festival.add_artist(ca.Artist("Kendrick Lamar",  2, e.Genre.HIPHOP,     e.StageSize.MAINSTAGE))
    festival.add_artist(ca.Artist("Norah Jones",     3, e.Genre.JAZZ,       e.StageSize.MEDIUM))
    festival.add_artist(ca.Artist("Arctic Monkeys",  4, e.Genre.ROCK,       e.StageSize.MAINSTAGE))
    festival.add_artist(ca.Artist("Dua Lipa",        5, e.Genre.POP,        e.StageSize.MAINSTAGE))

    print("\n── Booking Slots ──")
    festival.book_slot(2, e.StageSize.MAINSTAGE, day=1, start_time="22:00")
    festival.book_slot(4, e.StageSize.MAINSTAGE, day=2, start_time="22:00")
    festival.book_slot(5, e.StageSize.MAINSTAGE, day=3, start_time="22:00")
    festival.book_slot(1, e.StageSize.LARGE,     day=1, start_time="20:00")
    festival.book_slot(3, e.StageSize.MEDIUM,    day=2, start_time="18:00")

    # Try an invalid booking — stage too small
    print("\n── Invalid Booking Test ──")
    festival.book_slot(2, e.StageSize.SMALL, day=1, start_time="18:00")

    # Try a clash
    print("\n── Clash Test ──")
    festival.book_slot(5, e.StageSize.MAINSTAGE, day=1, start_time="22:00")

    #festival.save_to_json()

    #for x in festival["Artist"]:
    #    print(x)
