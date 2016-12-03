dmr_utils
_________

Utilities for working with Digital Moble Radio (DMR) in python. Includes routines for assembling and disasembling packets and encoding/removing FEC/ECC routines. The utilities are intended primarily for processing on the "network" side of DMR, not the air interface -- such as for building network linking tools, and as such, routines mostly remove FEC/ECC rather than appy repeairs, which should be done at the air interface first.

**Files in this repository and what they do**

const.py
  some stuff
  
utils.py
  some stuff
  
encode.py
  some stuff
  
decode.py
  some stuff
  
btpc.py
  Contains block product turbo code generators, extractors and related routines
  
    - decode_full_lc(_data) -- Extracts the useful LC data without checking for errors. Accepts one arguments of type bitarray and returns one item of type bitarray
  
crc.py
  some stuff
  
rs129.py
  some stuff
  
golay.py
  some stuff
  
hamming.py
  some stuff
  
qr.py
  some stuff
