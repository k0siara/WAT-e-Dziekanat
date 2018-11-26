# WAT e-Dziekanat
## Jak to działa?
Skrypt loguje się do systemu e-Dziekanat i pobiera plan zajęć do folderu, z którego go uruchomiono.
## Wymagania
#### [Python](https://www.python.org/downloads/)  
#### [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)  
### Biblioteki:
#### Selenium  
##### ``` pip install selenium ```

## Jak uruchomić?
- W folderze, w którym znajduje się skrypt umieść plik chromedriver.
- W pliku dane.txt wpisz swoje dane logowania do systemu e-Dziekanat:
```
username=TWÓJ LOGIN
password=TWOJE HASŁO
```

- Mając wypełniony ten plik możemy uruchomić skrypt poleceniem:  
#### ``` python script.py ```
