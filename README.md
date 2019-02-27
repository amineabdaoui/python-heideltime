# Python-HeidelTime
This is a python wrapper for the multilingual temporal tagger HeidelTime.

For more information about this tagger : https://github.com/HeidelTime/heideltime

Heideltime needs a Part Of Speech Tagger, by default it uses TreeTagger : http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/.
So you will need to install it and specify the treeTaggerHome in the config.props file.

# Usage

```
import HeidelTime
hw = HeidelTime.HeidelTimeWrapper('english')
hw.parse('Neil Armstrong was born in 1930')
```
