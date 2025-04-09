
# 🔐CryptoNada - Encryption Algorithms Collection - Python

This Python program is a comprehensive encryption tool that supports **15 classical encryption algorithms**, allowing users to **encrypt and decrypt** messages through an interactive command-line interface.

### 🧠 Features

- User-friendly interactive menu
- Supports encryption and decryption modes
- Includes classical and historical ciphers
- All functions are implemented using **pure Python**

### 🔒 Supported Algorithms

1. **Additive Cipher**  
2. **Multiplicative Cipher**  
3. **Affine Cipher**  
4. **Monoalphabetic Substitution Cipher**  
5. **Vigenère Cipher**  
6. **Autokey Cipher**  
7. **Playfair Cipher**  
8. **Hill Cipher**  
9. **One-Time Pad (OTP) Cipher**  
10. **Rotor Cipher**  
11. **Enigma-like Cipher**  
12. **Keyless Transposition**  
13. **Keyed Transposition**  
14. **Combined Transposition (Keyless + Keyed)**

### 📦 Requirements

- Python 3.x  
- `numpy` library (required for the Hill cipher)

To install dependencies:

```bash
pip install numpy
```

### 📥 How to Download & Use

Follow these steps to download and run the program on your local machine:

#### 1. Clone the repository:

To get the source code on your machine, you can clone the repository using `git`. Open your terminal (command prompt, PowerShell, or terminal in your IDE) and run:

```bash
git clone https://github.com/username/encryption-algorithms-python.git
```

Replace `username` with your GitHub username.

#### 2. Navigate to the project directory:

After cloning the repository, go into the project directory by running:

```bash
cd encryption-algorithms-python
```

#### 3. Install required dependencies:

To install the necessary Python libraries, use `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install `numpy` using:

```bash
pip install numpy
```

#### 4. Run the program:

Once all dependencies are installed, run the main script:

```bash
python encryption_program.py
```

This will start the interactive menu where you can choose the operation (encryption or decryption) and select the cipher to use.

### 📝 How to Use

After running the program, follow these steps:

1. **Choose the operation:**
   - Type `1` to encrypt a message.
   - Type `2` to decrypt a message.

2. **Select the cipher:**
   - Choose the cipher type by entering the number corresponding to the algorithm from the list (e.g., 1 for Additive Cipher, 2 for Multiplicative Cipher, etc.).

3. **Provide input:**
   - Enter the message you want to encrypt or decrypt.
   - Depending on the selected cipher, you may be asked to provide additional parameters (like a key or keyword).

4. **View the result:**
   - The program will display the encrypted or decrypted text.

### 📁 File Structure

```
encryption_program.py    # Main script with all algorithms
README.md               # This README file
requirements.txt        # List of dependencies
```

### 👩‍💻 Author

- **Nada Khaled** – Software Engineer & CEO And Founder Al-Eaqrab

### 🌐 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
