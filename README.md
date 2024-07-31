This repository contains PostScript examples useful for attacking Ghostscript.

For details see the corresponding blog post:
https://blog.redteam-pentesting.de/2023/ghostscript-overview/

## `print_version.ps`

Modified version of `print_version.ps` from [ghostinthepdf](https://github.com/neex/ghostinthepdf). Prints useful information about the configuration of Ghostscript.

## `list_files.ps`

Prints all filenames contained in the specified directory (by default `/tmp/`) to the output page.

### Variables

```
% how many chars per line at most
/charactercount 100 def

% Which directory should be listed
/target_directory (/tmp/*) def
```

## `print_file.ps`

Writes the content of the specified file to the page. The used function needs to be specified at the end of the code:

- `PrintFileBase64`: Prints files encoded as Base64 onto the page, useful for binary files.

```
(/usr/bin/bash) PrintFileBase64
```

- `PrintFileAsText`: Prints the content of files onto the page, respects newlines. Useful for simple text files, but binary files can also be printed if needed.

```
(/etc/passwd) PrintFileAsText
```

### Variables

```
% how many chars per line at most
/charactercount 100 def
```

## `embed_files_in_pdf.ps`

This script embeds all files in the specified directory (by default `/tmp/`) in the output PDF file using PDFMark.
Only works with `pdfwrite` device for that reason.
Use `extract_pdf_attachments.py` to extract all files from the PDF, or any capable PDF reader.

### Variables

```
% How many files can be included at most
/maxFileCount 100 def

% The folder with wildcard which will be embedded
/targetFolder (/tmp/*) def

% Enables printing error information to the page
/printErrors false def
```

## `long_running_embed_files.ps`

Similar to `embed_files_in_pdf.ps`, but runs for a specified amount of time and collects short-lived files by scanning the specified directory in regular intervals.

### Variables

```
% how often files should be checked
/totalRounds 1000 def

% How many milliseconds to sleep inbetween rounds
/sleepDuration 10 def

% How many files can be included at most
/maxFileCount 100 def

% The folder with wildcard which will be embedded
/targetFolder (/tmp/*) def

% Enables printing error information to the page
/printErrors false def
```

## `write_file.ps`

Writing files onto the disk. The used function needs to be specified at the end of the code:

- Writing plaintext: Useful for simple and short text file:

```
outfile (Output string which will be written to outfile) writestring
```

- `base64Decode`: Base64 decodes the input string. Useful for embedding (binary) files in PostScript. Decoding and writing to file:

```
(SGFsbG8gV2VsdAo=) base64Decode { outfile exch write } forall
```
