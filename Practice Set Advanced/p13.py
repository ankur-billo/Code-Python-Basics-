def print_all(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        
print_all(name="Alice",hello="Tu kon be?")