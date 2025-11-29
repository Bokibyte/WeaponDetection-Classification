# Utils

disini tempat menyimpan class khusus untuk menjalankan program. disini terdapat beberapa kelas yang krusial sebagai langkah untuk menjalankan sistem ini. sistem sengaja dipecah menjadi beberapa kelas dan method agar memudahkan saat debugging dan meningkatkan skalabilitas sistem.

## Classes

### - gitKeepGen

hanya class untuk menggenerate .gitkeep pada setiap folder kosong. gunanya agar folder tetap terpush ke github. fungsinya supaya sistem mudah dibaca

### - Preprocessing

`preprocess(inputPath, outputPath, classes)`

kelas utama yang menjalankan preprocessing data. hal ini bertujuan untuk meningkatkan akurasi model dengan menstrukturkan data yang belum sesuai. berikut penjelasan input:

> `inputpath`

yaitu path dimana dataset berada, atau lebuh tepatnya nama dataset. (harus dalam folder datasets)

> `outputPath`

nama hasil merapihkan dataset. (harus dalam folder datasets)

> `classes`

kalo ini diisi, maka akan menggenerate folder tambahan sesuai dengan kelas atau label yang akan dibuat

di kelas ini terdapat bebrapa method:

`createFolder`

membuat folder awal. jika ada classes maka akan generate folder dengan prefix kelas/label

`copyFile`

mengcopy file ke sesuai dengan struktur

kelas `cropBatch(datasetName, className, modelPath, padding)`

autocrop gambar agar meminimalisir noise untuk proses lanjutan. memiliki input:

> `datasetName`

nama atau path dataset (harus dalam folder datasets)

> `classname`

jika dataset awal memiliki kelas/label

> `padding`

padding crop gambar. default 0.

### - Organizer (opsional)

`Organizer(inputPath, movePath)`

kelas untuk merapihkan keluaran setelah run model. seperti memasukan kedalam folder sesuai dengan konteks. ini supaya rapih saja dan enak dibaca dan dipahami.

> `inputPath`

path keluaran hasil ai, biasanya ada di runs/

> `movePath`

### - Trainer

> `YOLOTrainer(modelPath)`

method "template" untuk train ai supaya settingnya bisa di pakai di model lain. menerima input berupa path dimana model berada (models/)

### -
