# Archi

This solution is based on the **appinum lib of python**.
The script simulates the human intervention with the android emulator.

# Requirements

- [appinum server](https://appium.io/)
- [android emulator]()
- [python 3.x](https://www.python.org/downloads/)

# in windows

### Prepare

- cd path\to\sr_facility_booking_android
- python -m venv .
- .\Scripts\activate.bat
- .\Scripts\pip.exe install -r .\requirement.txt

### Run:

python .\src\main.py -u **your_user** -t **yourpass[optional]** -f tennis -d '30' -ts '04:00 PM'
