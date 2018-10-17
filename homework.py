import hashlib

my_name = "d.galamaga"
m = hashlib.md5()
m.update(my_name.encode())

if __name__ == "__main__":
    print(f"Task completed by {Sergey.Krasilnikov}! md5 is {m.hexdigest()}")
