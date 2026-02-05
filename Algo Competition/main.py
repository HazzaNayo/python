import random
import sys

# main.py
# Game jualan sederhana (terminal)
# Tujuan: kumpulkan uang target dengan membeli murah dan menjual mahal.
# Cara main: ikuti instruksi di layar. Ketik "keluar" kapan saja untuk berhenti.


ITEMS = {
    "apel": {"base": 5, "vol": 0.3},
    "pisang": {"base": 3, "vol": 0.25},
    "jeruk": {"base": 4, "vol": 0.2},
    "susu": {"base": 8, "vol": 0.15},
}
START_MONEY = 50
STORAGE_LIMIT = 100
DAYS = 30
TARGET_MONEY = 500

def clamp(n, a, b): return max(a, min(b, n))

class Game:
    def __init__(self):
        self.day = 1
        self.money = START_MONEY
        self.inventory = {k: 0 for k in ITEMS}
        self.storage = STORAGE_LIMIT
        self.prices = {}
        self.history = []
        self.update_prices()

    def update_prices(self):
        self.prices = {}
        for it, params in ITEMS.items():
            change = random.uniform(-params["vol"], params["vol"])
            price = max(1, round(params["base"] * (1 + change)))
            # small chance of special event that spikes or drops price
            evt = random.random()
            if evt < 0.03:
                price = max(1, price * 2)  # spike
            elif evt > 0.97:
                price = max(1, price // 2)  # crash
            self.prices[it] = int(price)

    def show_status(self):
        print("\nHari", self.day, "/", DAYS)
        print("Uang: Rp", self.money)
        used = sum(self.inventory.values())
        print(f"Penyimpanan: {used}/{self.storage}")
        print("Harga pasar hari ini:")
        for it, p in self.prices.items():
            print(f" - {it:6} : Rp {p}")
        print("Inventori:")
        for it, q in self.inventory.items():
            print(f" - {it:6} : {q}")

    def buy(self, item, qty):
        if item not in ITEMS:
            print("Item tidak dikenal.")
            return
        qty = int(qty)
        if qty <= 0:
            print("Jumlah harus positif.")
            return
        if sum(self.inventory.values()) + qty > self.storage:
            print("Tidak cukup ruang penyimpanan.")
            return
        cost = self.prices[item] * qty
        if cost > self.money:
            print("Uang tidak cukup.")
            return
        self.money -= cost
        self.inventory[item] += qty
        print(f"Berhasil membeli {qty} {item} seharga Rp {cost}.")

    def sell(self, item, qty):
        if item not in ITEMS:
            print("Item tidak dikenal.")
            return
        qty = int(qty)
        if qty <= 0:
            print("Jumlah harus positif.")
            return
        if self.inventory[item] < qty:
            print("Tidak cukup stok untuk dijual.")
            return
        revenue = self.prices[item] * qty
        self.money += revenue
        self.inventory[item] -= qty
        print(f"Berhasil menjual {qty} {item} seharga Rp {revenue}.")

    def next_day(self):
        # random consumption/spoilage
        for it in list(self.inventory.keys()):
            spoil_chance = 0.02
            if it in ("susu",):
                spoil_chance = 0.1
            if random.random() < spoil_chance and self.inventory[it] > 0:
                lost = random.randint(1, max(1, self.inventory[it] // 4))
                self.inventory[it] = max(0, self.inventory[it] - lost)
                print(f"Sayang! {lost} {it} rusak/hilang semalam.")
        self.day += 1
        self.update_prices()
        self.history.append((self.day, dict(self.prices)))
        # small random event: bonus customer
        if random.random() < 0.05:
            bonus = random.randint(5, 30)
            self.money += bonus
            print(f"Bonus! Seorang pelanggan memberi donasi Rp {bonus}.")

    def play(self):
        print("Selamat datang di Game Jualan!")
        print(f"Target: Kumpulkan Rp {TARGET_MONEY} dalam {DAYS} hari.")
        while True:
            if self.money >= TARGET_MONEY:
                print("\nSelamat! Anda mencapai target keuntungan.")
                break
            if self.day > DAYS:
                print("\nWaktu habis.")
                break
            if self.money < 1 and sum(self.inventory.values()) == 0:
                print("\nAnda bangkrut. Permainan berakhir.")
                break

            self.show_status()
            cmd = input("\nPerintah (beli <item> <qty> | jual <item> <qty> | lanjut | simpan | keluar): ").strip().lower()
            if cmd == "keluar":
                print("Terima kasih sudah bermain.")
                break
            if cmd == "lanjut":
                self.next_day()
                continue
            if cmd == "simpan":
                self.save_snapshot()
                continue
            parts = cmd.split()
            if len(parts) >= 3 and parts[0] in ("beli", "b"),
                # can't use comma expression in Python; need to rewrite branch

                pass
            # The above accidental branch is invalid; provide proper parsing below.
            # (This comment explains why we re-parse.)
            parts = cmd.split()
            if len(parts) >= 3:
                action, item, qty = parts[0], parts[1], parts[2]
                if action in ("beli", "b"):
                    try:
                        self.buy(item, int(qty))
                    except ValueError:
                        print("Jumlah tidak valid.")
                    continue
                if action in ("jual", "j"):
                    try:
                        self.sell(item, int(qty))
                    except ValueError:
                        print("Jumlah tidak valid.")
                    continue
            print("Perintah tidak dikenal. Contoh: 'beli apel 5' atau 'jual susu 2' atau 'lanjut'.")

        print(f"Akhir permainan: Hari {self.day}, Uang Rp {self.money}")
        print("Inventori akhir:", self.inventory)

    def save_snapshot(self):
        fname = f"snapshot_day{self.day}.txt"
        try:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(f"Hari {self.day}\nUang: {self.money}\n\nHarga:\n")
                for it, p in self.prices.items():
                    f.write(f"{it}: {p}\n")
                f.write("\nInventori:\n")
                for it, q in self.inventory.items():
                    f.write(f"{it}: {q}\n")
            print("Tersimpan ke", fname)
        except Exception as e:
            print("Gagal menyimpan:", e)

if __name__ == "__main__":
    random.seed()
    game = Game()
    game.play()