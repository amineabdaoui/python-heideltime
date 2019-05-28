# Python-HeidelTime

This is a python wrapper for the multilingual temporal tagger HeidelTime.

For more information about this temporal tagger, please visit : https://github.com/HeidelTime/heideltime

Heideltime needs a Part Of Speech Tagger, by default it uses TreeTagger : http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/.
This repo includes TreeTagger scripts for Mac and Linux. Windows users will have to download the appropriate scripts from the TreeTagger home page.

# Demo

1. Clone the current github repo: `git clone https://github.com/amineabdaoui/python-heideltime`
2. Install its requirements: `pip install -r requirements.txt`
3. Create a python file in the same directory with the following code:
```python
import HeidelTime
hw = HeidelTime.HeidelTimeWrapper('english')
hw.parse('Neil Armstrong was born in 1930')
```

# Future Work
- Encapsulate the returned tagged string in a python object
- Find a way to install the appropriate POS tagger files according to the user OS.
- Package all the necessary parts in the same python package and release it on PyPi.

`Pull requests` are welcome to improve this wrapper (which is in an early stage).
