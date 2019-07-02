# gron.py

### Print JSON objects in a "Greppable" output.


# About The Project


This tool traverses a JSON object into a Greppable output. It's inspired by the original [Gron](https://github.com/tomnomnom/gron) tool written in Go-lang.

The algorithm I wrote is a depth-first tree traversing algorithm for traversing the JSON object. It’s done by recursively serializing the JSON object in order to complete the traversing process.


## Usage
```bash
$ cat test.json
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

$ gron test.json
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][GlossSeeAlso][0]->GML
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][GlossSeeAlso][1]->XML
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][para]->A meta-markup language, used to create markup languages such as DocBook.
[glossary][GlossDiv][GlossList][GlossEntry][GlossSee]->markup
[glossary][GlossDiv][GlossList][GlossEntry][Acronym]->SGML
[glossary][GlossDiv][GlossList][GlossEntry][GlossTerm]->Standard Generalized Markup Language
[glossary][GlossDiv][GlossList][GlossEntry][Abbrev]->ISO 8879:1986
[glossary][GlossDiv][GlossList][GlossEntry][SortAs]->SGML
[glossary][GlossDiv][GlossList][GlossEntry][ID]->SGML
[glossary][GlossDiv][title]->S
[glossary][title]->example glossary

$ # You can pipline input to gron too.

$ cat test.json | gron
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][GlossSeeAlso][0]->GML
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][GlossSeeAlso][1]->XML
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][para]->A meta-markup language, used to create markup languages such as DocBook.
[glossary][GlossDiv][GlossList][GlossEntry][GlossSee]->markup
[glossary][GlossDiv][GlossList][GlossEntry][Acronym]->SGML
[glossary][GlossDiv][GlossList][GlossEntry][GlossTerm]->Standard Generalized Markup Language
[glossary][GlossDiv][GlossList][GlossEntry][Abbrev]->ISO 8879:1986
[glossary][GlossDiv][GlossList][GlossEntry][SortAs]->SGML
[glossary][GlossDiv][GlossList][GlossEntry][ID]->SGML
[glossary][GlossDiv][title]->S
[glossary][title]->example glossary

$ cat test.json | gron | grep language
[glossary][GlossDiv][GlossList][GlossEntry][GlossDef][para]->A meta-markup language, used to create markup languages such as DocBook.

$ curl -s https://api.ipify.org?format=json | gron
[ip]->1.1.1.1
```

## Demo

[![asciicast](https://asciinema.org/a/254783.svg)](https://asciinema.org/a/254783)


### Installation

#### One-line installer

```bash
pip install git+https://github.com/mazen160/gronpy
```

#### Manual Installation
```
$ git clone https://github.com/mazen160/gronpy

$ cd gronpy && python3 setup.py install
```


# Requirements
* Python2 or Python3

## License
The project is currently licensed under MIT License.

# Legal Disclaimer
This project is made for educational and ethical testing purposes only. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.


# Author #
## *Mazin Ahmed* ##
* Website: [https://mazinahmed.net](https://mazinahmed.net)
* Email: *mazin [at] mazinahmed [dot] net*
* Twitter: [https://twitter.com/mazen160](https://twitter.com/mazen160)
* Linkedin: [http://linkedin.com/in/infosecmazinahmed](http://linkedin.com/in/infosecmazinahmed)
