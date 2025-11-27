import random

NUM_DICE = 6


# Ngeroll dua dadu sekaligus, hasilnya random 1–6
def roll_dice():
    return random.randint(1, NUM_DICE), random.randint(1, NUM_DICE)


# Ambil input angka dari user, kembalikan None kalau user ngaco
def get_guess(prompt):
    try:
        val = int(input(prompt))
        return val
    except ValueError:
        print("Masukin Angka! Broo -_- \n")
        return None


# Cek apakah dua tebakan user pas dengan dua hasil dadu (sesuai urutan)
def check_guess(g1, g2, d1, d2):
    return g1 == d1 and g2 == d2


# Validasi input yes/no; bakal looping sampai user bener
def ask_confirm(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans
        print("Salah Ketik -> Ketik [y/n] ")


# Ngecek apakah angka user masih dalam range dadu (1–NUM_DICE)
def in_range(value):
    return 1 <= value <= NUM_DICE


def guest_dice():
    while True:
        print("*" * 35)
        print("*** TEST YOUR LUCK!")
        print("=" * 25, "\n")

        player_name = input("Masukan Nama Anda : ").strip().title() or "Player"

        # Ambil dua input dari user
        guess1 = get_guess(f"Masukin tebakan dadu pertama [1-{NUM_DICE}] : ")
        guess2 = get_guess(f"Masukin tebakan dadu kedua [1-{NUM_DICE}] : ")

        # Kalau input bukan angka → ulang
        if guess1 is None or guess2 is None:
            continue

        # Validasi angka dalam range
        if not in_range(guess1) or not in_range(guess2):
            print(f"Angka cuma boleh 1 sampe {NUM_DICE} \n")
            continue

        cfm = ask_confirm(
            f"Tebakan Dadu ke 1 lu : {guess1}\nTebakan dadu ke 2 lu : {guess2} \nUdah yakin nihh? {player_name}, [y/n] ?\n"
        )

        # Keluar game kalau user batal
        if cfm == "n":
            print(f"Tengkyu udah main! {player_name}")
            break

        # Roll dadu
        die1, die2 = roll_dice()

        # Tampilkan hasil roll
        print(f"\n🎲 Hasil dadu keluar!\n - Dadu 1: {die1}\n - Dadu 2: {die2}\n")

        # Cek tebakan user
        if check_guess(guess1, guess2, die1, die2):
            print(
                f"🔥 GILA! {player_name}, tebakan lu **pas banget**! lu mantan judol suram apa gimana? 😂\n"
            )
        else:
            print(
                f"Belum hoki nih {player_name}. Coba lagi, siapa tau semesta mulai sayang. 😆\n"
            )

        play = ask_confirm(f"Masih Mau Main {player_name} [y/n] ? ")
        if play == "n":
            print(f"Oke mantep {player_name}, Tengkyu udah main! Cyaa! ✌️😁\n")
            break


if __name__ == "__main__":
    guest_dice()
