# slacki

[![Python](https://img.shields.io/pypi/pyversions/slacki)](https://img.shields.io/pypi/pyversions/slacki)
[![PyPI Version](https://img.shields.io/pypi/v/slacki)](https://pypi.org/project/slacki/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/slacki/blob/master/LICENSE)
[![Github Forks](https://img.shields.io/github/forks/erdogant/slacki.svg)](https://github.com/erdogant/slacki/network)
[![GitHub Open Issues](https://img.shields.io/github/issues/erdogant/slacki.svg)](https://github.com/erdogant/slacki/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/slacki/month)](https://pepy.tech/project/slacki/)
[![Downloads](https://pepy.tech/badge/slacki)](https://pepy.tech/project/slacki)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->


``Slacki`` is Python package for reading and posting in slack groups.

# 
**Star this repo if you like it! ⭐️**
#


### Installation
* Install slacki from PyPI (recommended). slacki is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```python
conda create -n env_slacki python=3.8
conda activate env_slacki
```

```bash
pip install slacki
```

#### Import slacki package
```python
from slacki import slacki
```

#### Example:
```python

# Import library
from slacki import slacki

from slacki import slacki
sc = slacki(channel='new_channel', token='xoxp-123234234235-123234234235-123234234235-adedce74748c3844747aed48499bb')

# Get some info about the channels
channels = sc.get_channels()

# Get some info about the users
users = sc.get_users()

# Send messages
queries=['message 1','message 2']
sc.post(queries)

# Snoozing
sc.snooze(minutes=1)

# Post file
sc.post_file(file='./data/slack.png', title='Nu ook met figuren uploaden :)')

# listen (retrieve only last message)
out = sc.retrieve_posts(n=3, retrieve_names=True)

```


#### Citation
Please cite slacki in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2020slacki,
  title={slacki},
  author={Erdogan Taskesen},
  year={2020},
  howpublished={\url{https://github.com/erdogant/slacki}},
}
```

#### References
* https://github.com/erdogant/slacki

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)
