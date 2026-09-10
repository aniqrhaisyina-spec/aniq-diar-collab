
def input_hasil_panen():
    hasil_panen = []

    jumlah_data = int(input("Jumlah data hasil panen: "))

    for i in range(jumlah_data):
        hasil = float(input(f"Hasil panen ke-{i+1}: "))
        hasil_panen.append(hasil)

    return hasil_panen
