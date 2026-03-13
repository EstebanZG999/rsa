from Crypto.PublicKey import RSA

def generar_par_claves(bits: int = 3072):

    if bits < 2048:
        raise ValueError("RSA debe usar al menos 2048 bits")

    key = RSA.generate(bits)

    public_key = key.publickey()

    private_pem = key.export_key(
        format="PEM",
        passphrase="lab04uvg",
        pkcs=8,
        protection="PBKDF2WithHMAC-SHA512AndAES256-CBC"
    )

    public_pem = public_key.export_key(format="PEM")

    with open("private_key.pem", "wb") as f:
        f.write(private_pem)

    with open("public_key.pem", "wb") as f:
        f.write(public_pem)
    

if __name__ == '__main__':
    generar_par_claves(3072)
    print("Claves generadas: private_key.pem y public_key.pem")