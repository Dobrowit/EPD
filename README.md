# EPD
Ewidencja pasa drogowego w QGIS.

Proste narzędzie do ewidencjonowania dokumentów w odniesieniu położenia obiektu na mapie.

Właściwie jest to gotowy projekt dla QGIS, który zawiera:
  - gotowe warstwy, które pobierają się na bierząco z geoportalu lub zasobów innej instytucji (tu Starostwo Powiatowe w Lęborku)
  - przykładową bazę ze skonfigurowanym formularzem i akcjami
  - szablon wydruku dla wybranego obiektu (wywoływanie poprzez akcję na obiekcie)

Projekt ma drobne udogodnienia takie jak:
  - przy wprowadzaniu obiektu do bazy wprowadzana jest automatycznie nazwa najbliższej ulicy oraz wyliczona powierzchnia (te dane oczywiście można zmieniać)
  - wydruk ma odrębny układ warstw i zawiera tylko wybrany obiekt, który można wybierać w oknie widoku (w trybie atlasu) po numerze dokumentu
  - do projektu załączono plik personalizacji interfejsu (do wczytania przez menu Ustawienia), który ukrywa zbędne przyciski i paski narzędzi
  - projekt nie używa wtyczek więc dla początkującego użytkownika można wyłączyć wszystkie wtyczki
  - zabieg z ukrywaniem funkcji ma na celu ułatwienie kożystania dla początkujących - QGIS w domyśłnej konfiguracji ma bardzo dużo przycisków, paneli i funkcji, które mogą nieobytą w QGIS osobę dezorientować
  - obiekty na mapie mają odpowiedni kolor w zależności od statusu ważności (np. umowy): przyszłe, bieżące i przeszłe

![Zrzut ekranu z 2024-10-19 07-34-06](https://github.com/user-attachments/assets/c8cf5e3a-f9b1-4eb0-b2fb-9031f9f3723e)
