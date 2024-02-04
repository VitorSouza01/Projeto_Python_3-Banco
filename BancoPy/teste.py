from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente("Felicity Jones", "felicity@gmail.com", "123.456.789-01", "01/01/1987")
angelina: Cliente = Cliente("Angelina Jolie", "angelina@gmail.com", "789.456.123-02", "10/10/1978")

print(felicity)
print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

print(contaf)
print(contaa)