dmr_utils
_________

Utilities for working with Digital Moble Radio (DMR) in python. Includes routines for assembling and disasembling packets and encoding/removing FEC/ECC routines. The utilities are intended primarily for processing on the "network" side of DMR, not the air interface -- such as for building network linking tools, and as such, routines mostly remove FEC/ECC rather than appy repeairs, which should be done at the air interface first.