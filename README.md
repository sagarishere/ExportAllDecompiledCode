# ExportAllDecompiledCode

I was reverse engineering a software and found that there was no easy way to communicate with LLM the pseudo-logic of c, extracted from Ghidra.

This script is made in Jython and is compatible with old Python 2.7 syntax.

Premise:

In the modern AI world, we need scripts that make it easy to extract data in combined form to be put into the unchained AIs. That's what this script does.

How to use:

In Ghidra, go to Windows, and Scripts Manager. There create a new script and select Jython, with name ExportAllDecompiledCode.py

Now just save and run the script. The prompt will ask you for filename to export, select the right folder you want it in and put in the name of the file you want it to be exports in.

I recommend something like, pseudocode.txt pr pseudocode.c

Now it will create the file and export the whole pseudocode.


Result:

Makes it extremely easy to get combined pseudocode of any binary. No need to read the function tree in assembly.

Author: [Sagar Yadav](https://linkedin.com/in/sagaryadav)
License: I release it under EUPL v1.2