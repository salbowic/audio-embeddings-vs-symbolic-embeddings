# Audio embeddings vs symbolic embeddings 

## 📌 Cel projektu
Projekt miał na celu zbadanie jakości i własności embeddingów muzyki symbolicznej generowanych przy pomocy enkodera CLaMP2 w stosunku do emebeddingów muzyki w formatacie audio uzyskiwanych przy pomocy OpenL3. 

## 🛠️ Metodologia
1. **Analiza literaturowa i bibliografia** 
    - ➡️ [design_proposal](project_files/design_proposal.md)

2. **Zbiory danych**:
-  Przygotowanie zbiorów danych muzycznych w formacie symbolicznym (MIDI) oraz w audio (WAV)[[opis](project_files/analysis.md)].
    - gtzan
    - instrumenty

3. **Generacja embeddingów**:
   - Interfejs do **audio embeddings** używa modelu [OpenL3](https://github.com/marl/openl3).
   - Interfejs do **symbolic embeddings** używa modelu [CLaMP2](https://github.com/sanderwood/clamp2).

4. **Testy**:
    - Porównanie pomiędzy modelami embeddingów zredukowanych za pomocą PCA oraz TSNE.
    - Wyliczenie i porównanie centroidów dla zredukowanych embeddigów dla poszczególnych modeli.
    - Dla wyznaczonych średnich embeddingów dla każdej kategorii obliczenie i porównanie miar cosinusowych pomiędzy nimi.
    - Zbadanie średniej wariancji embedingów wygenerowanych dla poszczególnych kategorii w badanych zbiorach.

    \* Wszystkie testy zostały wykonane z wykorzystaniem GPU GeForce RTX3060 12GB od NVIDIA z cuda w wersji 11.2. 
5. **[Analiza wyników](project_files/analysis.md)**

## 🔧 Instalacja & używanie
**Instalacja**
```bash
# Klonowanie repozytorium
git clone https://gitlab-stud.elka.pw.edu.pl/wniemir1/audio-embeddings-vs-symbolic-embeddings.git

# Przygotowanie i uruchomienie środowiska
conda env create -f music_emb_gen_env.yml
conda activate music_emb_gen_env

```

Uzyskanie wag do modelu clamp2.

Wagi do model clamp 2 należy pobrać ze strony [Hugging Face](https://huggingface.co/sander-wood/clamp2/blob/main/weights_clamp2_h_size_768_lr_5e-05_batch_128_scale_1_t_length_128_t_model_FacebookAI_xlm-roberta-base_t_dropout_True_m3_True.pth).

Następnie należy je umieścić w folderze: 
```bash
Clamp2/clamp2_github/code
```

**Używanie**

W celu przetworzenia danego zbioru danych z różnymi rodzajami dźwięków, należy zadbać o odpowiednią strukturę folderów. Pliki należy umieścić w odpowiednich folderach z nazwą odpowiadającą ich rodzajowi, a wszystkie foldery różnych rodzajów zamieścić w jednym głównym folderze. Należy również pamiętać o odpowiednich formatach danych (`.wav`, `.ogg` lub `.flac` dla OpenL3 oraz `.midi` lub `.mid` dla Clamp2), których nie rozdzielamy na różne foldery. Przykładowa struktura odpowiednio przygotowanego zbioru danych wygląda następująco:
```
📦 audio-embeddings-vs-symbolic-embeddings
├── 📁 songs
    ├── 📁 hiphop
    ├── ...
    ├── 📁 rock
        ├── rock_song1.mid
        ├── rock_song1.wav
        ├── rock_song2.mid
        ├── rock_song2.wav
        ├── ...
```
Uruchomienie programu z przykładowymi parametrami z pliku ex_params.txt:
```bash
 python main.py --params-file ex_params.txt
```

Plik tekstowy z parametrami można edytować według własnych potrzeb, a sam program można również uruchomić za pomocą komendy podając odpowiednie parametry (np. --dataset \<dataset_dir\>):
```bash
python main.py --dataset songs --emb-methods both --emb-dir results/embeddings/songs --input-repr mel256 --embedding-size 512 --plot Plot both results/songs/plots --calc-metrics results/songs/plots results/songs/variance
```

## 📂 Struktura projektu
```
📦 audio-embeddings-vs-symbolic-embeddings
├── 📁 Clamp2
    ├── 📁 clamp2_github                    # folder z https://github.com/sanderwood/clamp2
        ├── 📁 code
            ├── weights_clamp2(...)         # wagi modelu clamp2
            ├── ...
        ├── ... 
    ├── clamp2_embedding_generator.py       # klasa do generowania embeddingów clamp2
    ├── test_clamp2.py                      # plik do uruchamiania testów na clamp2
├── 📁 OpenL3        
    ├── openl3_embedding_generator.py       # klasa do generowania embeddingów openL3
    ├── test_openl3.py                      # plik do uruchamiania testów na openl3
├── 📁 results                         
├── 📁 project_files                        # analizy i dokumentacje
├── ex_params.txt                           # przykładowe parametry
├── main.py                                 # główny plik uruchomieniowy do testów
├── music_emb_gen_env.yml                   # plik do tworzenia środowiska
├── README.md                               # opis projektu
```
