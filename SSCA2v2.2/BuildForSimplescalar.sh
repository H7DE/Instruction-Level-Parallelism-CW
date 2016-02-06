#!/bin/bash

# This script overcomes a yucky bug in simplescalar's GCC, which 
# prevents it from working on the user filesystem (due to a problem 
# with the transition to 64-bit).  Luckily /tmp is implemented differently 
# and doesn'thave this problem so we copy the tree there and do the make there.

TMPNAME=/tmp/SSCA2v2.2-$USER
rm -rf $TMPNAME

# make clean here to avoid confusion
make clean

echo Copying the tree to $TMPNAME so we can build it there
cp -rf ../SSCA2v2.2 $TMPNAME

# now make it in the /tmp directory
pushd $TMPNAME
make CC=/homes/phjk/simplescalar/bin/gcc AR=/homes/phjk/simplescalar/bin/sslittle-na-sstrix-ar RANLIB=/homes/phjk/simplescalar/bin/sslittle-na-sstrix-ranlib
popd

# and link the binary back here
ln -s $TMPNAME/SSCA2 
