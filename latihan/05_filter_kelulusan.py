# Filter nilai yang lulus (>= 60) menggunakan perulangan dan seleksi
nilai = [75, 55, 80, 60, 45, 90]
lulus = []
for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")