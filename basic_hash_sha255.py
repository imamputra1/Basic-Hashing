import hashlib

class BasicHasher:
    """
    kita akan membuat sebuah kelas sederhana yang melakukan hashing pada tipe data string.
    pertama kita akan membungkus fungsionalitas dari module 'haslib' python.
    alasanya karena ini memungkinkan kita membuat sebuah objek hasher untuk diterpakan dan 
    dikonfigurasi dengan menggunakan algoritma tertentu misalnya: SHA 256.

    penggunaan kelas yang kita lakukan memudahkan dalam mengorganisasikan code. daripada memanggil
    fungsi hashlib terus menerus dibanyak tempat. kita bisa membuat instance dar kelas ini dan memanggil
    methodnya. agar kode kita lebih bersih dan mudah dikelola.
    """
    def __init__(self, algoritma: str = "sha256") -> None:
        """
        __init__ adalah sebuah method build-in dari python untuk melakukan constructor untuk kelas ini.
        method ini akan dieksekusi ketika kita membuat sebuah objek baru dari kelas ini.
        ini menerima 1 argumen opsional 'algoritma'.

        tujuannya adalah untuk mengatur 'state'(keadaan) internal objek.
        kita menyimpan algoritma sha256 atau md5 didalam self.algoritma sehingga method lain(hash_data) tau 
        algoritma mana yang harus digunakan

        Args: 
            algoritma (str): nama algoritma yang ingin digunakan harus berupa nama yang dikenali oleh library
            hashlib seperti SHA256, MD5, SHA512. 
        """
        if algoritma not in hashlib.algorithms_available:
            raise ValueError(f"Algoritma tidak dikenali: {algoritma}")

        self.algoritma: str = algoritma
        print(f"basic hasher diinisialisasi dengan algoritma: {self.algoritma}")
    
    def hash_data(self, data: str) -> str:
        """
        Menghasilakan hash hexsadesimal dari data  yang diberikan
        method ini akan mengambil input dan merubah menjadi bytes, menghashnya dengan algoritma yang disimpan
        dan mengembalikan dalam bentuk hash sebagai string hexsadesimal

        ini adalah core dari class ini. kita akan mengambalikan 'hexdigest' karena ini adalah format paling umum
        untuk menampilkan atau menyimpan hasil hash

        Args:
            data(str): data input
        Return: 
            hash dari data dengan hexsadesimal string
        """
        hasher = hashlib.new(self.algoritma)
        data_bytes: bytes = data.encode('utf-8')
        hasher.update(data_bytes)
        hashed_output: str = hasher.hexdigest()
        """
        1. membaut sebuah objek hash berdasarkan algoritma yang pilih dengan menggunakan 'hashlib.new()'.
        new() adalah sebuah method yang ada didalam modelu hashlib yang merupakan std lib python.
        ini akan secara dinamis untuk memudahkan kita memilih algoritma hash berdsarkan nama string.

        2. mengubah data string menjadi bytes dengan pengkodean UTF-8, alasanya karena algoritma hashing
        beroprasi pada level bytes bukan karakter atau string, mereka tidak tau apa itu'a' atau 'b'
        namun mereka hanya tau representasi bytesnya. kita menggunakan UTF-8 karena merupaka standar umum.

        3. lalu kita akan memasukan data byte kedalam object hasher yang sudah kita buat dengan method update().
        ini akan memperoses data kita. ctt: update() adalah method build-in.

        4. lalu setelah proses selesai kita akan mengemalikanya kedalam format string hexsadesimal dengan hexdigest.
        ini akan mengembalikan dengan format yang bisa kita baca. kemudian disimpan divariable hashed_output.
        """
        return hashed_output

