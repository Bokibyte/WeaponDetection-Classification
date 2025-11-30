## **1. Folder `curve/`**

Folder ini berisi grafik metrik selama proses training. Metrik ini digunakan untuk memantau apakah model membaik atau overfitting. (ini untuk di detection)

### **• BoxF1_curve.png**

Grafik F1-score untuk bounding box. Menggambarkan keseimbangan antara precision dan recall sepanjang training.

### **• BoxP_curve.png**

Grafik precision dari deteksi bounding box. Precision tinggi berarti prediksi positif jarang salah (sedikit false positive).

### **• BoxR_curve.png**

Grafik recall dari bounding box. Recall tinggi berarti model jarang melewatkan objek (sedikit false negative).

### **• BoxPR_curve.png**

Kurva hubungan antara Precision–Recall. Biasanya menampilkan trade-off untuk threshold confidence tertentu.

## **2. Folder `result/`**

Folder ini menyimpan hasil evaluasi akhir model.

### **• confusion_matrix.png**

Matrix yang menunjukkan berapa banyak prediksi klas yang benar maupun salah untuk setiap kelas.

### **• confusion_matrix_normalized.png**

Versi normalisasi dari confusion matrix (biasanya dalam persen). Lebih mudah dibaca ketika jumlah sampel tidak seimbang.

### **• results.csv**

File tabel yang memuat semua metrik per-epoch (precision, recall, mAP, loss, dll). Berguna untuk analisis lanjutan.

### **• results.png**

Plot gabungan dari berbagai metrik training (loss, mAP, precision, recall) dalam satu grafik.

## **3. Folder `train/`**

Memuat sampel visualisasi hasil training.

### **• train_batch*.jpg**

Gambar batch selama training yang berisi:

- Bounding box ground truth (label asli)
- Bounding box prediksi awal dari model pada epoch tersebut

Ini membantu memverifikasi apakah augmentasi berjalan benar dan apakah model mulai memahami objek.

## **4. Folder `val/`**

Sama seperti folder `train/` tetapi untuk validation dataset.

### **• val_batch*_labels.jpg**

Menampilkan label ground truth pada data validasi.

### **• val_batch*_pred.jpg**

Menampilkan hasil prediksi model pada validation set.

Ini sangat penting untuk mengecek apakah model generalisasi dengan baik ke data yang tidak dilihat saat training.

## **5. Folder `weights/`**

Folder yang menyimpan model hasil training.

### **• best.pt**

Model terbaik berdasarkan metrik tertentu (biasanya mAP). **Ini yang biasanya kamu gunakan untuk inference.**

### **• last.pt**

Model pada epoch terakhir, tidak selalu yang terbaik.

## **6. File `args.yaml`**

Berisi semua konfigurasi training:

- Path dataset
- Hyperparameter (lr, batch, epochs)
- Ukuran gambar
- Device (CPU/GPU)
- Augmentasi

File ini berguna untuk mereplikasi training dengan tepat di kemudian hari.

# **Ringkasan Singkat**

| Bagian              | Fungsi                                                   |
| ------------------- | -------------------------------------------------------- |
| **curve/**    | Grafik metrik training (precision, recall, F1, PR curve) |
| **result/**   | Confusion matrix + hasil evaluasi model                  |
| **train/**    | Visualisasi batch training                               |
| **val/**      | Visualisasi batch validation                             |
| **weights/**  | File model (`best.pt` & `last.pt`)                   |
| **args.yaml** | Config lengkap training                                  |
