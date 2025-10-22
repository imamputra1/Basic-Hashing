from typing import Any, Optional
class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        """
        Self table adalah sebuah List utama(U) yang akan menampung list kita, list didalam List-U adalah kita sebut sebagai bucket.
        backet akan memuat pasangan key dan value dalam sebuah tuple.
        ex: [("key", value), (,), dst] --> diinsiasi sebagai bucket 0
            [(,), (,)] --> bucket 1
        """
        self.table: list[list[tuple[Any, Any]]] = [[] for _ in range(size)]
    
    def _hash(self, key: Any) -> int:
        return hash(key) % self.size

    def put(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if  k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key: Any) -> Optional[Any]:
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

if __name__ == "__main__":
    hash_table = HashTable(size= 5)
    
    hash_table.put("nama", "putra")
    hash_table.put("usia", 23)
    hash_table.put("kota", "jogja")

    print(hash_table.get("nama"))
    print(hash_table.get("usia"))
    
    hash_table.put("usia", 25)
    print("-" * 10, "sesudah valuenya diganti", "-" * 10,
          f"\n setelah value umur diganti {hash_table.get("usia")}")


