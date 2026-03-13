# Laboratorio RSA

Proyecto de laboratorio para estudiar el uso de RSA en un escenario de transferencia de documentos legales entre oficinas. El repositorio cubre tres partes principales:

- Generacion de claves RSA en formato PEM.
- Cifrado y descifrado directo con RSA-OAEP para mensajes pequenos.
- Cifrado hibrido usando RSA-OAEP + AES-256-GCM para documentos de tamano arbitrario.

El escenario simula una plataforma de transferencia de documentos confidenciales donde RSA protege la clave simetrica y AES-GCM cifra el contenido real del documento.

## Estructura del proyecto

- `generar_claves.py`: genera el par de claves RSA y exporta `private_key.pem` y `public_key.pem`.
- `rsa_OAEP.py`: realiza una prueba de cifrado y descifrado directo con RSA-OAEP.
- `rsa_AES_GCM.py`: implementa el esquema hibrido RSA-OAEP + AES-256-GCM.

## Requisitos

- Python 3.10 o superior
- `pycryptodome`

## Instalacion

1. Clonar el repositorio:

```bash
git clone <URL-del-repositorio>
cd rsa
```

2. Crear y activar un entorno virtual opcional:

```bash
python -m venv .venv
```

En Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install pycryptodome
```

## Uso

### 1. Generar claves RSA

Este script genera un par de claves RSA y las guarda en formato PEM:

- `private_key.pem`
- `public_key.pem`

Ejecucion:

```bash
python generar_claves.py
```

### 2. Probar cifrado y descifrado con RSA-OAEP

Este script carga las claves generadas, cifra un mensaje de prueba y luego lo descifra con la clave privada.

Ejecucion:

```bash
python rsa_OAEP.py
```

### 3. Probar cifrado hibrido RSA-OAEP + AES-256-GCM

Este script cifra un documento usando AES-GCM y luego cifra la clave AES con RSA-OAEP. 

Ejecucion:

```bash
python rsa_AES_GCM.py
```

## Flujo esperado del laboratorio

1. Ejecutar `generar_claves.py` para crear las claves RSA.
2. Ejecutar `rsa_OAEP.py` para validar el cifrado directo de mensajes pequenos.
3. Ejecutar `rsa_AES_GCM.py` para cifrar documentos de tamano arbitrario con el esquema hibrido.

## Ejemplos de ejecucion

### Ejemplo 1: generar claves

```bash
python generar_claves.py
```

### Ejemplo 2: cifrar un mensaje con RSA-OAEP

```bash
python rsa_OAEP.py
```

### Ejemplo 3: cifrar un documento con RSA + AES-GCM

```bash
python rsa_AES_GCM.py
```

## Preguntas de analisis

### 1. ¿Explique por qué no cifrar el documento directamente con RSA?
No es recomendable cifrar los documentos directamente con RSA ya que este algoritmo fue hecho para cifrar datos por pequeñas cantidades, no archivos grandes como los documentos en este caso. El cifrado RSA utiliza operaciones matematicas complejas lo cual hace que el proceso de cifrado sea computacionalmente costoso y lento cuando se aplica a grandes volumenes de datos. Asimismo, el RSA tiene un tamaño limite del mensaje que puede cifrar, esto vuelve impractico cifrar documentos completos como PDFs. 

### 2. Estructura de un archivo PEM

### 3. Por que RSA-OAEP produce resultados distintos al cifrar el mismo mensaje

### 4. RSA en protocolos reales: TLS 1.3, certificados X.509 y SSH
