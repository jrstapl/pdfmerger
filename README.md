# pdfmerger
### Author: Joshua Stapleton

Simple script to merge pdfs written in Python with PyPDF. Provided an input directory or series of filenames, create a single, merged PDF file. See [arguments](#arguments) for list of input options. 

## Installation

Clone this repository to your local machine:

```bash
git clone git@github.com:jrstapl/pdfmerger.git
```

Recomended: Use with ```anaconda```, ```venv``` or other environment management tool. 

Requirements: ```Python >= 3.8```

This project uses [poetry](https://python-poetry.org/docs/#installation) for installation.

Use ```poetry``` to install the project by running the ```install``` command in the directory containing the pyproject.toml file:

```bash
poetry install
```


## Use

The pyproject.toml file includes a script to run this project as CLI. The list of arguments is provided below.

### Arguments

<style>
table th:first-of-type {
    width: 10%;
}
table th:nth-of-type(2) {
    width: 10%;
}
table th:nth-of-type(3) {
    width: 50%;
}
table th:nth-of-type(4) {
    width: 30%;
}
</style>

|Argument           |Abbreviation   |Description    |
|:------------------|:---------------:|:---------------|
|--filenames|-f             |Individual filenames, specified multiple times, once for each file|
|--directory    |-d             |Directory to be searched for *.pdf files. Can be modified with --recursive [-r] to search all subdirectories|
|--recursive    |-r             |Search all subdirectories in provided directory (must be used with --directory [-r]). Uses Path.rglob(\*.pdf) instead of Path.glob(\*.pdf)|
|--output       |-o             |Merged output file. If used with --filenames [-f], must be specified. If --directory [-d] is used, the default is to output "merged.pdf" within that directory if no output is provided.|



## Examples

### Merge speficied pdf files:
```bash
MergePDF -f /path/to/file1.pdf -f /path/to/file2.pdf -o /path/to/merged.pdf
```

### Merge pdf files in top-level directory
```bash
MergePDF -d /path/to/directory (optional)<-o /path/to/merged.pdf>
```

### Merge all pdf files in sub-directories
```bash
MergePDF -d /path/to/directory -r (optional)<-o /path/to/merged.pdf>
```


