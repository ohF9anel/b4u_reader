B4U reader for Python
=============

This library parses .b4u files, which are the native format of [Before You Know It](http://www.byki.com/), a great flashcard application.

Many B4U files can be downloaded from http://www.byki.com/listcentral.html.

Usage
------------
    python readb4u.py [filename]

will read the file [filename] and create a KVTML (Parley) representation, with separate .OGG (sound) and .JPEG (image) files as available in the original .b4u file, in the folder `output`, with the name `cards.kvtml`.

To create HTML file look in the python code (last lines). 
