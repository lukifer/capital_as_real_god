# Essays on Capital as a Real God

Conversion of the following blog essays to Markdown, PDF, and ebooks, with permission of the author:

1. https://ianwrightsite.wordpress.com/2020/09/03/marx-on-capital-as-a-real-god-2/
2. https://ianwrightsite.wordpress.com/2021/11/25/dark-eucharist-of-the-real-god/

### Files

- ePub: [essays_on_capital_as_a_real_god.epub](https://github.com/lukifer/capital_as_real_god/essays_on_capital_as_a_real_god.epub)
- PDF: [essays_on_capital_as_a_real_god.pdf](https://github.com/lukifer/capital_as_real_god/essays_on_capital_as_a_real_god.pdf)
- Markdown: [essays_on_capital_as_a_real_god.md](https://github.com/lukifer/capital_as_real_god/essays_on_capital_as_a_real_god.md)
- Kindle*: [essays_on_capital_as_a_real_god.mobi](https://github.com/lukifer/capital_as_real_god/essays_on_capital_as_a_real_god.mobi)

(* Untested Calibre conversion)

### ePub creation

ePub code modified from [https://github.com/AlexPof/mark2epub](https://github.com/AlexPof/mark2epub)

```
python -m venv .venv
source .venv/bin/activate
pip3 install markdown
python3 mark2epub.py ./mds/essays_on_capital_as_a_real_god essays_on_capital_as_a_real_god.epub
```

### PDF creation

```
brew install pandoc
brew install weasyprint
pandoc essays_on_capital_as_a_real_god.md -o essays_on_capital_as_a_real_god.pdf --pdf-engine=weasyprint
```