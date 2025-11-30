main file untuk menjalankan seluruh method ada pada `command.py` .

proses fleksibel. artinya hanya 1x semua harus dijalankan, setelah itu bebas mau makai proses yang mana. ada 6 method yang dipanggil:

- ``nwPrep()``

untuk preprocessing. 

> ![!WARNING]
>
> hanya dipakai jika dataset tidak rapih

- ``runTrain()``

untuk train dengan model yang sudah ditentukan beserta setting pada `trainer.py` sebelumnya

- `organize()`

untuk merapihkan keluaran train ke folder yang dikehendaki. dan ini masih harus dama direktori runs/

- `cropTs()`

memotong gambar dengan cara melakukan pengulangan untuk semua kelas senjata dengan bantuan dari weight hasil train model deteksi.

- `isWeapon()`

untuk melakukan deteksi apakah senjata atau bukan pada dataset. disini dataset yang diambil image nya untuk di deteksi adalah gun_detection. langkahnya adalah dengan mengambil seluruh image pada dataset dan dilakukan pengulangan untuk cek satu satu apakah file senjata atau bukan dengan memanggil method `isWeap()` dari kelas `ImageUtilities` .

- ``imageClazzy()``

melakukan pengulangan  untuk mengambil gambar yang sudah di crop. lalu mengambil nama gambar, memasukan kedalam method `.getBest()` dan `.saveToFolder` dari kelas `imageUtilities.` output awal berupa teks nama file dari nama gambar yang diambil, dan kelas mana yang cocok, beserta skornya.
