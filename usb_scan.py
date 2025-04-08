
**📄 usb_scan.py**
```python
import subprocess

def usb_geraete_auflisten():
    output = subprocess.check_output("lsusb", shell=True)
    print("Angeschlossene USB-Geräte:\n")
    print(output.decode())

usb_geraete_auflisten()
