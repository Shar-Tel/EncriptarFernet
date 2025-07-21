
from cryptography.fernet import Fernet
 

 
#Sencillo programa que encripta o desencripta un texto mediante encriptación Fernet
 



def pideEoD():
    """Espera a que pulses E o D"""
    encDes=input("Encriptar(E)/Desencriptar(D)")
    if encDes.upper()=="E":
        return "E"
    if encDes.upper()=="D":
        return "D"
    print("Por favor pulse E o D")
    return pideEoD()
    
 
#La clave de la encriptación Fernet. Debe ser igual al encriptar y desencriptar. Si hace falta, el código comentado genera una clave nueva. 
# key = Fernet.generate_key()
# print(key)
fernet = Fernet(b'VWEa5nNFsOU0q3yGheKFeAyLvYzKW4206QFQERUzI0o=')


while True:
    texto=input("Texto a encriptar o desencriptar: ")
    entrada=pideEoD()
    if entrada=="E":
        encMessage = fernet.encrypt(texto.encode())
        print("Texto encriptado: ", encMessage)
    else:
        tmpTexto=texto.replace("b'","") 
        tmpTexto=bytes(tmpTexto,'utf-8')
        decMessage = fernet.decrypt(tmpTexto).decode()
        print("Texto desencriptado: ", decMessage)        
    input("Pulse una tecla para continuar")    
