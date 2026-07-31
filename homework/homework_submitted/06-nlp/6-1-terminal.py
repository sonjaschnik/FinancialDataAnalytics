@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ cd casestudy
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/casestudy (main) $ git add pdf_downloader.py
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/casestudy (main) $ git commit -m "add pdf_downloader.py"
[main 5d9936f] add pdf_downloader.py
 1 file changed, 15 insertions(+)
 create mode 100644 casestudy/pdf_downloader.py
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/casestudy (main) $ git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 643 bytes | 643.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   4bcac8e..5d9936f  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/casestudy (main) $ cd /
@sonjaschnik ➜ / $ cd workspaces/01-setup-sonjaschnik
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ mkdir homeworks
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ touch homeworks/.gitkeep
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ git add .
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ git commit -m "add folder homeworks"
[main a534338] add folder homeworks
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homeworks/.gitkeep
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 328 bytes | 328.00 KiB/s, done.
Total 4 (delta 1), reused 2 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   5d9936f..a534338  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik (main) $ cd homeworks
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ pip install pdfminer.six
Collecting pdfminer.six
  Downloading pdfminer_six-20260107-py3-none-any.whl.metadata (4.3 kB)
Requirement already satisfied: charset-normalizer>=2.0.0 in /home/codespace/.local/lib/python3.12/site-packages (from pdfminer.six) (3.4.5)
Collecting cryptography>=36.0.0 (from pdfminer.six)
  Downloading cryptography-48.0.0-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.3 kB)
Requirement already satisfied: cffi>=2.0.0 in /home/codespace/.local/lib/python3.12/site-packages (from cryptography>=36.0.0->pdfminer.six) (2.0.0)
Requirement already satisfied: pycparser in /home/codespace/.local/lib/python3.12/site-packages (from cffi>=2.0.0->cryptography>=36.0.0->pdfminer.six) (3.0)
Downloading pdfminer_six-20260107-py3-none-any.whl (6.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 35.1 MB/s  0:00:00
Downloading cryptography-48.0.0-cp311-abi3-manylinux_2_34_x86_64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 62.3 MB/s  0:00:00
Installing collected packages: cryptography, pdfminer.six
Successfully installed cryptography-48.0.0 pdfminer.six-20260107

[notice] A new release of pip is available: 26.0.1 -> 26.1.2
[notice] To update, run: python3 -m pip install --upgrade pip
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ from pdfminer.high_level import extract_text
bash: from: command not found
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdfminer.high_level import extract_text
>>> extracted_text = extract_text('../lit/nonanswers.pdf')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/codespace/.python/current/lib/python3.12/site-packages/pdfminer/high_level.py", line 172, in extract_text
    with open_filename(pdf_file, "rb") as fp, StringIO() as output_string:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/codespace/.python/current/lib/python3.12/site-packages/pdfminer/utils.py", line 46, in __init__
    self.file_handler: AnyIO = open(filename, *args, **kwargs)  # noqa: SIM115
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '../lit/nonanswers.pdf'
>>> print(extracted_text[0:80])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'extracted_text' is not defined. Did you mean: 'extract_text'?
>>> exit()
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git add .
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git commit -m "upload nonanswers.pdf"
[main bbf16fd] upload nonanswers.pdf
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homeworks/nonanswers.pdf
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.28 MiB | 2.17 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   a534338..bbf16fd  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdfminer.high_level import extract_text
>>> extracted_text = extract_text('../homeworks/nonanswers.pdf')
>>> print(extracted_text[0:80])






































>>> exit()
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ pip install pymupdf
Collecting pymupdf
  Downloading pymupdf-1.27.2.3-cp310-abi3-manylinux_2_28_x86_64.whl.metadata (24 kB)
Downloading pymupdf-1.27.2.3-cp310-abi3-manylinux_2_28_x86_64.whl (25.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 25.0/25.0 MB 63.5 MB/s  0:00:00
Installing collected packages: pymupdf
Successfully installed pymupdf-1.27.2.3

[notice] A new release of pip is available: 26.0.1 -> 26.1.2
[notice] To update, run: python3 -m pip install --upgrade pip
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import fitz
>>> doc = fitz.open("nonanswers.pdf")
>>> for page in doc:
... print(page.get_text())
  File "<stdin>", line 2
    print(page.get_text())
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> print(doc.page_count)
37
>>> find . -name "*.pdf"
  File "<stdin>", line 1
    find . -name "*.pdf"
           ^
SyntaxError: invalid syntax
>>> find . -name "nonanswers.pdf"
  File "<stdin>", line 1
    find . -name "nonanswers.pdf"
           ^
SyntaxError: invalid syntax
>>> find . -nonanswers "*.pdf"
  File "<stdin>", line 1
    find . -nonanswers "*.pdf"
           ^
SyntaxError: invalid syntax
>>> import fitz
>>> doc = fitz.open("deine_datei.pdf")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/codespace/.python/current/lib/python3.12/site-packages/pymupdf/__init__.py", line 2992, in __init__
    raise FileNotFoundError(f"no such file: '{filename}'")
pymupdf.FileNotFoundError: no such file: 'deine_datei.pdf'
>>> for page in doc:
...     print(page.get_text())
[1]+  Stopped                 python3
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ import fitz
bash: import: command not found
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ doc = fitz.open("nonanswers.pdf")
bash: syntax error near unexpected token `('
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ doc = fitz.open("nonanswers.pdf"))
bash: syntax error near unexpected token `('
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import fitz
>>> doc = fitz.open("nonanswers.pdf")
>>> for page in doc:
...     print(page.get_text())
... 
MuPDF error: library error: zlib error: invalid code lengths set


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


MuPDF error: library error: zlib error: incorrect header check


>>> exit()
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git add .
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git commit -m "add homework 6"
[main 7b03bc5] add homework 6
 1 file changed, 92 insertions(+)
 create mode 100644 homeworks/6-nlp.ipynb
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git push

Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.04 KiB | 1.04 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   bbf16fd..7b03bc5  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ 
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git add .
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git commit -m "add ruben_2021_eft"
[main d9911ac] add ruben_2021_eft
 2 files changed, 8 deletions(-)
 create mode 100644 homeworks/ruben_2021_eft.pdf
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 2 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 459.03 KiB | 18.36 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   7b03bc5..d9911ac  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ from pdfminer.high_level import extract_text
bash: from: command not found
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdfminer.high_level import extract_text
>>> extracted_text = extract_text('../homeworks/ruben_2021_eft.pdf')
>>> print(extracted_text[0:80])
Volume 11 No 01 – April 2024 – ISSN (Online): 2355-7435 

Available Online to ht
>>> from pdfminer.high_level import extract_text
>>> extracted_text = extract_text('../homeworks/nonanswers.pdf')
>>> print(extracted_text[0:80])






































>>> exit()
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git add .
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git commit -m "add a second paper on eft"
[main d712734] add a second paper on eft
 2 files changed, 2 insertions(+), 7 deletions(-)
 create mode 100644 homeworks/lagoarde-segot_2021_eft.pdf
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 2 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.26 MiB | 3.94 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   d9911ac..d712734  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdfminer.high_level import extract_text
>>> extracted_text = extract_text('../homeworks/lagoarde-segot_2021_eft.pdf')
>>> print(extracted_text[0:80])
Contents lists available at ScienceDirect 

International Review of Financial An
>>> exit()
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ touch pdf_extractor.py
code pdf_extractor.py
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3 pdf_extractor.py > output.txt
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ python3
Python 3.12.1 (main, Mar 11 2026, 12:17:56) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> pdf_extractor.py > output.txt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pdf_extractor' is not defined
>>> exit()
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git add pdf_extractor.py
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git commit -m "add pdf extractor script"
[main 1fb0e6a] add pdf extractor script
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homeworks/pdf_extractor.py
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 326 bytes | 326.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iwh-halle/01-setup-sonjaschnik
   d712734..1fb0e6a  main -> main
@sonjaschnik ➜ /workspaces/01-setup-sonjaschnik/homeworks (main) $ 