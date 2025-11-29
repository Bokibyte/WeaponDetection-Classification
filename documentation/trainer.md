# Template Trainer

> **`data = f"datasets/{dataPath}"`**

Path menuju dataset YOLO. YOLO akan membaca struktur dataset dan menentukan kelas, lokasi train/val, serta membaca gambar.

- **Dampak ke akurasi:** bukan parameter tuning.
- **Dampak ke kecepatan:** dataset besar jadi loading lebih lama.

> **`epochs`**

Jumlah iterasi pelatihan. Semakin besar `epochs`, model semakin belajar namun risiko overfitting meningkat.

- **Akurasi:** naik jika dataset kecil, stabil kalau augmentasi kuat.
- **Kecepatan:** bertambah linear sesuai jumlah epoch.

> `imgsz`

Ukuran input gambar (contoh: 224, 448, 512).

- **Akurasi:** gambar lebih besar → fitur lebih detail → akurasi naik.
- **Kecepatan:** ukuran gambar lebih besar = GPU lebih berat = training lebih lambat.

> `device `

Menentukan apakah pakai CPU atau GPU.

- `0` → GPU
- `cpu` → CPU

> `workers`

Jumlah thread CPU untuk pemuatan data.

- **Akurasi:** tidak berpengaruh.
- **Kecepatan:** workers lebih banyak = loading data lebih cepat.

> `optimizer = "AdamW"`

Optimizer yang dipakai dalam update bobot.

- **AdamW** adalah versi Adam dengan weight decay yang lebih stabil.
- Cocok untuk dataset kecil-sedang.

**Dampak:**

- **Akurasi:** lebih stabil dibanding SGD, cepat konvergen.
- **Kecepatan:** sedikit lebih lambat daripada SGD namun lebih presisi.

> `lr0 = 0.0005`

Learning rate awal.

- Learning rate kecil → training lebih stabil, cocok dataset kecil.
- Learning rate besar → cepat belajar, tapi mudah divergen.

**Dampak:**

- **Akurasi:** LR kecil=lebih bagus untuk dataset kecil.
- **Kecepatan:** LR kecil = butuh lebih banyak epoch untuk mencapai konvergensi.

> `dropout = 0.1`

Menonaktifkan 10% neuron secara acak saat training.

- Mengurangi overfitting.
- Sangat berguna jika dataset kecil.

**Dampak:**

- **Akurasi:** bisa naik jika dataset kecil, turun sedikit jika dataset besar.
- **Kecepatan:** sedikit lebih lambat karena operasi dropout.

> `patience = 20`

Early stopping: berhenti jika tidak ada peningkatan selama 20 epoch.

- Mencegah overfitting.
- Menghemat waktu training.

**Dampak:**

- **Akurasi:** mencegah model belajar terlalu lama sampai merusak performa.
- **Kecepatan:** training jauh lebih cepat jika model sudah konvergen.

> `hsv_s = 0.3`

Random perubahan saturasi.

- membuat warna lebih kaya/lebih pudar secara acak

**Efek:**

- **Akurasi:** dataset kecil → sangat bagus
- **Kecepatan:** minimal

> `hsv_v = 0.3`

Random perubahan brightness (value).

- Meniru kondisi gelap, terang, backlight.

**Efek:**

- **Akurasi:** signifikan untuk kondisi real-world
- **Kecepatan:** kecil

> `fliplr = 0.5`

Flip horizontal dengan probabilitas 50%.

**Efek:**

- **Akurasi:** naik drastis untuk object rigid (senjata).
- **Kecepatan:** sangat kecil.

> `scale = 0.2`

Zoom in/out acak sebesar ±20%.

- Bikin model lebih tahan jarak kamera berbeda.

**Efek:**

- **Akurasi:** sangat naik
- **Kecepatan:** augmentasi realtime (dampak kecil)

## Ringkasan


| Parameter   | Dampak Akurasi | Dampak Kecepatan    |
| ----------- | -------------- | ------------------- |
| AdamW       | ⭐⭐⭐⭐       | ⭐⭐⭐              |
| lr0 0.0005  | ⭐⭐⭐⭐       | ⭐                  |
| dropout 0.1 | ⭐⭐⭐         | ⭐⭐                |
| patience 20 | ⭐⭐⭐         | ⭐⭐⭐⭐⭐          |
| hsv_h/s/v   | ⭐⭐⭐         | ⭐                  |
| fliplr      | ⭐⭐⭐⭐       | ⭐                  |
| scale 0.2   | ⭐⭐⭐⭐       | ⭐⭐                |
| imgsz besar | ⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐ (lambat) |
| batch besar | ⭐⭐⭐         | ⭐⭐⭐⭐            |
| workers     | -              | ⭐⭐⭐⭐            |

---
