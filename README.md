# PORTFOLIO

Projekt ma budowę modułową, każda aplikacja działa jako niezależny segment.

## ManyMailBox

Zintegrowana z bazą danych, obsługa wielu skrzynek mailowych w jednym miejscu.
Początkowo projektowana do obsługi wielu formularzy kontatkowych na róznych stronach. 
Agregowane dane mogą być wykorzystwane n.p. do celów statystycznych i marketingowych.

### Funkcjonalności

- Odczyt ze skrzynek w standardzie `IMAP` oraz `POP`
- Automatyczne parsowanie maili
- Obłsuga kodowania/dekodowania (`ISO-8859-2`,` ISO-8859-1`)
- Zapisywanie maili jako obiektów bazie danych.
- Automatyczne przekazywanie zapisanych wiadomości na zdefiniowane adresy mailowe.

### Wymagane paczki

- django
- pillow
- mail-parser
- imap-tools
