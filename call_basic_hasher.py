from basic_hash_sha255 import BasicHasher

print("-" * 18,"Contoh SHA256", "-" * 18)
hasher_sha256 = BasicHasher()

input_data1: str = "Rahasia saya"
hash1: str = hasher_sha256.hash_data(input_data1)
print("--- detail hash ---\n", f"input asli: {input_data1}\n hasil Hash: {hash1}\n panjang hash: {len(hash1)} karakter")

input_data2: str = "aku cinta kamu"
hash2: str = hasher_sha256.hash_data(input_data2)
print("--- detail hash ---\n", f"input asli: {input_data2}\n hasil Hash: {hash2}\n memerikas panjang hash apakah sama: {hash1 == hash2}")

input_data3: str = "Rahasia saya"
hash3: str = hasher_sha256.hash_data(input_data3)
print("--- detail hash ---\n", f"input asli: {input_data2}\n hasil Hash: {hash3}\n memerikas panjang hash apakah sama: {hash1 == hash3}")

print("\n" * 2)
print("-" * 18, "Contoh MD5", "-" * 18)
hasher_md5 = BasicHasher("md5")

input_data4: str = "Nino dan Putra"
hash4: str = hasher_md5.hash_data(input_data4)
print("--- detail hash ---\n", f"input asli: {input_data4}\n hasil Hash: {hash4}\n memerikas panjang hash apakah sama: {len(hash4)} karakter")
