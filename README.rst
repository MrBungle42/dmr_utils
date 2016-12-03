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
  
- *decode_full_lc(_data):* Extracts the useful FULL LC data without checking for errors. Accepts one argument of type bitarray and returns one item of type bitarray.

- *interleave_19696(_data):* Accepts one argument of type bitarray and returns a bitarray interlieaved.

- *encode_19696(_data):* Accepts an LC as a 12-byte string (LC and RS1293 FEC) encodes it into a 196bit bitarray and builds the proper row and column structure with hamming codes and returns a type bitarray

- *encode_header_lc(_lc):* Accpets LC data as a bitarray, applies the header mask and appends RS1293 FEC, encodes BPTC19696, interleaves for transmition. Returns a type bitarray that is the full DMR LC header packet.

- *encode_terminator_ls(_lc):* Accepts LC data as a bitarray, applies the terminator mask and appends RS1293 FEC, encodes BPTC19696, interleaves for transmition. Returns a type bitarray that is the full DMR LC terminator packet.

- *decode_emblc(_elc):* Extracts the useful EMBEDDED LC data without checking for errors. Accepts a type bitarray and returns type string.

- *encode_emblc(_lc):* Accepts 12 byte LC as a string, adds 5-byte checksum, adds row hamming bits, column partiy bits and arranges the matrix for transmission. Returns a type dict with 4 key/value pairs. Keys 1-4 are DMR bursts b-e respectively, such that burst "B" is key 1's associated value and so on.
  
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
