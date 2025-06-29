#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀              𓐓  ex26-28.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/06/29 00:17:46 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/06/29 00:56:40 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
import numpy as np


# ===[ main: ]=================================================================
def main():
    # 26. python built-in sum() -1 + 0 + 1 + 2 + 3 + 4 = 9
    print(sum(range(5), -1))
    # 26. numpy built-in sum() 4 + 3 + 2 + 1 + 0 = 10
    print(np.sum(range(5), -1))

    # 27. Checking the allowed expressions
    Z = np.array([1, 2, 3])
    print(f"Z: {Z}")
    print(f"Z**Z: {Z**Z}: Allowed")
    # 27. Bitwise Operators (shiftting) 2 << [1, 2, 3] >> 2
    print(f"2 << Z >> 2: {2 << Z}: Allowed")
    # 27. Z <-Z: Invalid Syntax but Z < -Z is valide
    print("Z <- Z: Not Allowed, Invalid Synatax")
    # 27. 1j: imaginary unit, representing sqrt(-1)
    print(f"1j*Z: {1j * Z}: Allowed")
    # 27. devision by 1 two times (Z / 1) / 1 => Z
    print(f"Z/1/1: {Z/1/1}: Allowed")
    # 27. Comparing (Z < Z) and result with > Z => [ Flase, False, ...]
    # Ambigous You have to add paranthisis
    print(f"Z<Z>Z: {(Z < Z) > Z}: Not Allowed")

    # 28. RunTime Error 0/0 => return np.nan
    print(f"np.array(0) / np.array(0): {np.array(0) / np.array(0)}")
    # 28. RunTime Error 0/0 => return 0
    print(f"np.array(0) // np.array(0): {np.array(0) // np.array(0)}")
    # 28. Runtime error, invalid value (nan) to cast => -9.22337204e+18
    print(f"np.array([np.nan]).astype(int).astype(float): {
          np.array([np.nan]).astype(int).astype(float)}")


if __name__ == '__main__':
    main()
