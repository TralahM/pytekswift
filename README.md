
[![Build Status](https://travis-ci.com/TralahM/pytekswift.svg?branch=master)](https://travis-ci.com/TralahM/pytekswift)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a/branch/master?svg=true)](https://ci.appveyor.com/project/TralahM/pytekswift/branch/master)
[![Documentation Status](https://readthedocs.org/projects/pytekswift/badge/?version=latest)](https://pytekswift.readthedocs.io/en/latest/?badge=latest)
[![License: GPLv3](https://img.shields.io/badge/License-GPLV2-green.svg)](https://opensource.org/licenses/GPLV2)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![Views](http://hits.dwyl.io/TralahM/pytekswift.svg)](http://dwyl.io/TralahM/pytekswift)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pytekswift/pull/)
[![GitHub pull-requests](https://img.shields.io/badge/Issues-pr-red.svg?style=flat-square)](https://github.com/TralahM/pytekswift/pull/)
[![Language](https://img.shields.io/badge/Language-python-3572A5.svg)](https://github.com/TralahM)
<img title="Watching" src="https://img.shields.io/github/watchers/TralahM/pytekswift?label=Watchers&color=blue&style=flat-square">
<img title="Stars" src="https://img.shields.io/github/stars/TralahM/pytekswift?color=red&style=flat-square">
<img title="Forks" src="https://img.shields.io/github/forks/TralahM/pytekswift?color=green&style=flat-square">

# pytekswift.


[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)

# Documentation

[![Documentation](https://img.shields.io/badge/Docs-pytekswift-blue.svg?style=for-the-badge)](https://github.com/TralahM/pytekswift)

ISO 9362 defines a standard format of Business Identifier Codes (also known as SWIFT-BIC, BIC, SWIFT ID or SWIFT code) approved by the International Organization for Standardization (ISO).
It is a unique identification code for both financial and non-financial institutions.
The acronym SWIFT stands for the Society for Worldwide Interbank Financial Telecommunication.
The ISO has designated SWIFT as the BIC registration authority.
When assigned to a non-financial institution, the code may also be known as a Business Entity Identifier or BEI.
These codes are used when transferring money between banks, particularly for international wire transfers, and also for the exchange of other messages between banks.
The codes can sometimes be found on account statements.

## Structure.

The previous edition is ISO 9362:2009 (dated 2009-10-01).
The SWIFT code is 8 or 11 characters, made up of:

- 4 letters: institution code or bank code.
- 2 letters: ISO 3166-1 alpha-2 country code (exceptionally, SWIFT has assigned the code XK to Republic of Kosovo, which does not have an ISO 3166-1 country code)
- 2 letters or digits: location code
    * if the second character is "0", then it is typically a test BIC as opposed to a BIC used on the live network.
    * if the second character is "1", then it denotes a passive participant in the SWIFT network
    * if the second character is "2", then it typically indicates a reverse billing BIC, where the recipient pays for the message as opposed to the more usual mode whereby the sender pays for the message.
- 3 letters or digits: branch code, optional ('XXX' for primary office)

Where an eight digit code is given, it may be assumed that it refers to the primary office.


# How to Install
```bash
# In terminal do:
$ pip install pytekswift
```

## Building from Source for Developers

```console
$ git clone https://github.com/TralahM/pytekswift.git
$ cd pytekswift
$ python setup.py install
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the license here](LICENSE)


# Self-Promotion

[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-red?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-red.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://org.tralahtek.com)


