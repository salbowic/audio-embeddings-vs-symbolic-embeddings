# WIMU Projekt (Design Proposal) - Audio embeddings vs symbolic embeddings 

## Cel Projektu

Projekt ma na celu zbadanie jakości i własności embeddingigów muzyki symbolicznej generowanych przy pomocy enkodera CLaMP (CLIP) w stosunku do emebedingów muzyki w formatacie audio uzyskiwanych przy pomocy OpenL3. 

## Zespół

* ID zespołu: 4
* Członkowie: 
    * Wiktor Niemirski
    * Sebastian Albowicz 
    * Andrzej Sawicki 

## Harmonogram

* **Tydzień 4** (21-27 października)
    * Przegląd bibliografii, uzupełnienie i odświeżenie wiedzy z zakresu tematu projektu
    * Zbudowanie solidnej podstawy wiedzy na temat embeddingów symbolicznych (CLaMP) i audio (OpenL3) w kontekście cech związanych ze stylem muzycznym i technikami kompozycyjnymi.

* **Tydzień 5** (28 października - 3 listopada)
    * Wstępne przygotowanie eksperymentów i konfiguracja środowiska.
        * Skonfigurowanie środowiska deweloperskiego.
        * Zainstalowanie na środowisku wymaganych bibliotek potrzebnych do wykorzystania modeli.
        
* **Tydzień 6** (4-10 listopada)
    * Spreparowanie odpowiednich zbiorów danych z dźwiękami i fragmentami muzycznymi (zarówno symbolicznymi, jak i audio), które są potrzebne do eksperymentów.
    * Przetworzenie danych do pożądanych formatów.

* **Tydzień 7** (11-17 listopada)
    * Testy działania modeli o zagnieżdzeniach muzyki symbolicznej oraz muzyki w formatach audio dla pojedynczych przykładów
    * **funkcjonalny prototyp projektu** - _przeanalizowana literatura, podstawowe skrypty do generacji testów, wstepny zbiór danych_

* **Tydzień 8** (18-24 listopada)

    * Przerwa spowodowana nieobecnością jednego z członków oraz kolokwium

* **Tydzień 9** (25 listopada - 1 grudnia)
    * Opracowanie interfejsów testowych do używanych modeli

* **Tydzień 10** (2-8 grudnia)
    * Wizualizacja embeddingów dla przygotowanych przykładów ze zbiorów danych
    * Wyznaczenie metryk dla uzyskanych zagnieżdżeń w celu porównania i wyciągniecia wniosków

* **Tydzień 11** (9-15 grudnia)
    * Badania i rozwiązywanie ewentualnych problemów
    
* **Tydzień 12** (16-22 grudnia)
    * Podsumowanie badań i sformułowanie wniosków

* **Tydzień 13** (23-29 grudnia)
    * Przerwa świąteczna

* **Tydzień 14** (30 grudnia - 5 stycznia)
    * Ostateczne poprawki i oddanie projektu

## Bibliografia

* https://ieeexplore.ieee.org/document/8682475 - Artykuł OpenL3 (2019)
* https://arxiv.org/abs/2304.11029 - Artykuł CLaMP (2023)
* https://arxiv.org/pdf/2410.13267 - Artykuł CLaMP2 (2024)
* "Analiza porównawcza głębokich osadzeń plików muzycznych w reprezentacji symbolicznej oraz audio" - Piotr Szachewicz 2024 - praca analizująca podobny teamat (analiza ilościowa)

## Analiza literaturowa
| Nazwa  | Komentarz       | Link   |
| :---: | --- | :---: |
| "LOOK, LISTEN, AND LEARN MORE: DESIGN CHOICES FOR DEEP AUDIO EMBEDDINGS"    |   Artykuł o OpenL3 (2019)<br>W badaniu autorzy podkreślają, jak różne wybory projektowe, takie jak architektura sieci czy sposoby uczenia, wpływają na jakość reprezentacji i ich przydatność w zadaniach takich jak klasyfikacja stylów czy analiza nastroju. OpenL3 tworzy i paruje embeddingi dla materiałów wideo i odpowiadających im materiałów audio. W naszym projekcie wykorzystamy tylko wytwarzanie embeddingów audio w formacie .wav.   | https://ieeexplore.ieee.org/document/8682475 |
| CLaMP    |  Artykuł CLaMP (2023) <br> Artykuł wprowadzający model CLaMP pretrenowany metodą kontrastywnego uczenia na parach tekstu i muzyki. CLaMP operuje na muzyce symbolicznej w formacie ABC oraz na tekście głównie w języku angielskim. Dzięki modelu CLaMP możemy dokonywać takich zadań jak przeszukiwanie semantyczne lub klasyfikacja danych do wcześniej nie wyuczonych kategorii. Autorzy deklarują lepsze możliwości od powstałych modeli do daty opublikowania artykułu. CLaMP składa się z dwóch enkoderów: tekstowego RoBERTa oraz muzycznego M3, oba bazują na architekturze Transformera. | https://arxiv.org/abs/2304.11029  | 
| CLaMP2       |   Artykuł CLaMP2 (2024) <br> Artykuł wprowadzający CLaMP2, będący drugą iteracją modelu CLaMP. CLaMP2 podobnie jak jego poprzednik operuje na formatach symbolicznych oraz na tekście, jednak w tej odsłonie autorzy rozwiązali problem braku wielojezyczności modelu. Autorzy użyli GPT4 do rozszerzenia, odszumienia i ogólne polepszenia zbiorów trenujących (które są głównie w języku angielskim). Enkder M3 został wzbogacony o przetwarzanie MIDI, zostało na nim przeprowadzone szeregu ulepszeń zwiększających możliwości reprezentacji danych muzycznych, enkoder tworzy embeddingi o rozmiarze 768 oraz może przetwarzań na wejściu na raz do 32768 znaków.| https://arxiv.org/pdf/2410.13267 |
|"Principal component analysis: a review and recent developments"|Artykuł o PCA(2016)<br> Opisuje popularną metodę wynalezioną już w 1901, służącą do redukcji wymiarowości dużych zbiorów danych zwaną Analiza głównych składowych (ang. principal component analysis). PCA pozwala na przekształcenie złożonych danych do prostszej postaci, bez znaczącej utraty informacji. Dzięki PCA dane są łatwiejsze do interpretacji. W projekcie PCA zostanie wykorzystane do przetworzenia wielowymiarowych zagnieżdżeń do dwuwymiarowej postaci, którą można przedstawić na wykresie. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4792409/pdf/rsta20150202.pdf|
|"Visualizing Data using t-SNE"|Artykuł o t-SNE (2008)<br> Opisuje nowszą od PCA (bo wynalezioną w 2008r.) technike wizualizacji wielowymiarowych danych. T-SNE również umożliwia przedstawić dane w dwu lub trójwymiarowej przestrzeni. Metoda ta działa na bazie SNE (Stochastic Neighbor Embedding), ale jest znacznie łatwiejsza w optymalizacji i zwraca zauważalnie lepsze wizualizacje, poprzez redukcje tendencji do grupowania punktów razem na środku przestrzeni. W artykule opisane jest, czym wyróżnia się ta metoda i dlaczego jest najlepsza ze wszystkich technik w tworzeniu pojedynczej mapy, która ukazuje strukture danych w wielu różnych skalach. NA potrzeby projektu t-SNE posłuży jako druga z metod (obok PCA), służących do przekształcenia wielowymiarowych embeddingów do postaci interpretowalnej przez człowieka na wykresie.  | https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf
| "Analiza porównawcza głębokich osadzeń plików muzycznych w reprezentacji symbolicznej oraz audio" | Praca magisterka napisana na Poltechnice Warszawskie WEiTI. (2024) <br> Autor wskazał kluczową rolę wyboru algorytmów redukcji wymiarów w swoich badaniach. Autor reporuje że algorytm T-SNE daje lepsze wyniki niż PCA. Zostałą przedstawiona lekka przewaga modelu CLaMP nad modelem OpenL3, jedank uzyskane wyniki nie były w pełni zadowalające, autor podjerzewał że zbiór danych jest niekoniecznie dobrze potagowany, ale też zaznaczył  stratę informacji podczas redukcji wymiarów wspomnianymi algorytmami. Wynikiem pracy było potwierdzenie hipotez o podobnej zdoloności wychwytu cech zarówno przez model działający na muzyce symbolicznej co czystym audio.| PDF | 
| Music transcription modelling and composition using deep learning | Artykuł o FolkRNN (2016) <br> FolkRNN to rekurencyjna sieć neuronowa zaprojektowana do generowania muzyki ludowej w formacie ABC na podstawie istniejących transkrypcji muzycznych. Model wykorzystuje sekwencyjny charakter muzyki, umożliwiając generowanie zarówno nowych utworów, jak i wariacji istniejących melodii. FolkRNN stał się istotnym narzędziem w analizie i generacji muzyki tradycyjnej, pokazując, jak sztuczna inteligencja może wspierać badania nad muzyką etnograficzną​. | https://arxiv.org/abs/1604.08723 |
| Music Transformer | Artykuł o Music Transformer (2018) <br> Artykuł wprowadza model Music Transformer, który wykorzystuje mechanizm uwagi (self-attention) do generacji muzyki symbolicznej z zachowaniem długoterminowej struktury. Tradycyjne podejścia, takie jak rekurencyjne sieci neuronowe, często nie radzą sobie z modelowaniem odległych zależności w muzyce. Music Transformer został wykorzystany do generacji nowych utworów na podstawie fragmentów muzycznych (motywów), co umożliwia twórcze rozwijanie pomysłów muzycznych. | https://arxiv.org/abs/1809.04281 | 
| Multitrack Music Transformer | Artykuł o MMT (2022) <br> Wprowadzenie modelu MMT, który pozwala na generację muzyki wielościeżkowej w formacie MIDI, uwzględniając różnorodne instrumenty i style muzyczne. Eksperymenty wykazały, że większe ograniczenia wprowadzone do modelu (np. dostarczenie fragmentu referencyjnego) poprawiają jakość generowanej muzyki. Model demonstruje wysoki poziom spójności i różnorodności w generowanych utworach. | https://arxiv.org/abs/2207.06983 | 
| Frechet Music Distance: A Metric For Generative Symbolic Music Evaluation | Artykuł o FMD (2024) <br> Artykuł wprowadza Fréchet Music Distance (FMD) jako nowy wskaźnik oceny jakości generatywnej muzyki symbolicznej. Jest to adaptacja istniejących metryk, takich jak Fréchet Inception Distance (FID) dla obrazów i Fréchet Audio Distance (FAD) dla muzyki audio, zaprojektowana specjalnie dla domeny muzyki symbolicznej (np. MIDI). FMD stanowi pierwszy wskaźnik dedykowany ocenie muzyki symbolicznej, ułatwiając precyzyjną i skalowalną ocenę modeli generatywnych w tej dziedzinie. Artykuł ma na celu ustanowienie standardu dla przyszłych badań w generatywnej muzyce symbolicznej. | PDF | 


## Zakres eksperymentów
Naszym celem jest zbadanie, czy embeddingi muzyki symbolicznej oraz audio zawierają podobne informacje, które pozwalają na rozróżnienie takich cech, jak styl muzyczny czy nastrój utworu. W ramach badania wygenerujemy pary embeddingów dla modeli CLaMP i OpenL3, które następnie zostaną zwizualizowane oraz przeanalizowane za pomocą odpowiednich metryk. Na podstawie przetworzonych reprezentacji wyciągniemy wnioski, które będą rezultatem naszych badań.

## Funkcjonalność programu
Program nie będzie zawierał interfejsu graficznego, a będzie miał formę wykonywalnych skryptów dla zaplanowaych testów i badań. Przygotowany skrypt wygeneruje wizualizacje badanych zagnieżdżeń oraz wartości poszczególnych metryk, które będą podstawą do rozważań i wyciągania wniosków o badanych technologiach.

## Stack technologiczny
- OpenL3 (PyTorch) - https://github.com/marl/openl3/tree/main
- CLaMP (TensorFlow) - https://github.com/xuzhang1199/CLAMP
- Pyenv lub Conda - zarządzanie środowiskami i biblotekami
- Docker - zarządzanie sterownikami i poprawna instalcja bibliotek
- narzędzia do wizualizacji - matplotlib
- narzędzia do redukcji wymiarów embedingów - algorytm PCA, LLE, flatten
- narzędzia do wyliczania miar - scipy, scikit-learn
- ewentualna potrzeba wykorzystania GPU do badań na bardzo dużych zbiorach danych

## Dataset
Link do zbioru danych: https://wutwaw-my.sharepoint.com/:u:/g/personal/01149756_pw_edu_pl/EY1kJ_hN1HNDrvAL3yXZpy4BThoQnlQKXy83cS2a7LuxDA?e=ter2pf
