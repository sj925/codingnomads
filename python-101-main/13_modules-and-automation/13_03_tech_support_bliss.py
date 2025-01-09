# Use the built-in `platform` module to print out the following info:
import platform

print(f"{'Platform:':>10} {platform.platform()}")  # Shows your OS platform
print(f"{'Compiler:':>10} {platform.python_compiler()}")  # Shows Python compiler
print(f"{'Python:':>10} {platform.python_version()}")  # Shows Python version
print(f"{'System:':>10} {platform.system()}")  # Shows OS name
print(f"{'Release:':>10} {platform.release()}")  # Shows OS release
print(f"{'System:':>10} {platform.processor()}")  # Shows processor type