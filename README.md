# Scanner

This is a very simple threaded port scanner I built in a couple hours. This is not meant to be used as a an actual tool (although it could be), this is a showcase. This is no were close to a final product, it was made in a couple hours.

## Usage

### Downloading

Clone this repository and cd into it

```
git clone https://github.com/emit07/scanner
cd scanner
```

### Parameters

The paramteres are in a specific order because I have not impleamented the argparse lib. The paramteres are as follow

* `HOST` : The host ip to scan the ports in
* `THREADS` : The amount of threads used to scan ports (the more the better but takes more cpu power)
* `RANGE` : The range in which to scan the ports

An example of arguments would be as such

`python3 scanner.py 10.0.0.15 100 100 1000`

If ran without parameters the default are as follow

* `HOST` : Your Machine IP
* `THREADS` : 100
* `RANGE` : 0, 100