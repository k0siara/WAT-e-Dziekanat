<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Logo_WAT.jpg" width="150" align="right">

# WAT e-Dziekanat
Skrypt loguje się do systemu e-Dziekanat i pobiera plan zajęć do folderu, z którego go uruchomiono.
## Wymagania:
* [Python](https://www.python.org/downloads/)  
* [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)  
### Biblioteki:
* Selenium  
##### ``` pip install selenium ```

## Instalacja:
```bash
1. git clone https://github.com/k0siara/WAT-e-Dziekanat.git
2. cd WAT-e-Dziekanat
```
- Umieść plik [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) w folderze, w którym znajduje się skrypt.
- W pliku login_data.txt wpisz swoje dane logowania do systemu e-Dziekanat:
```
username=TWÓJ LOGIN
password=TWOJE HASŁO
```

- Mając wypełniony plik, możemy uruchomić skrypt poleceniem:  
#### ``` python script.py ```
