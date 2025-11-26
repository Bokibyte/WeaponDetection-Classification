## Dimana hasil train?

- kalo hasil untu detection ada di `runs/detecttion/train/weights/`
- kalo hasil untu classification ada di `runs/classification/<class senjata>/train/weights/`

biasanya ambil `best.pt`

## Bagaimana alur kerja model?

ini sebenernya model deteksi semua, cuman kita tweak bagian model klasifikasi sebagai alat pembanding

## Kenapa datasets kosong?

karena dikecualikan dari push github untuk menghindari beban up. jadi kalian pakai yang sudah jadi aja
