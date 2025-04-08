from pypdf import PdfWriter
from pathlib import Path
from argparse import ArgumentParser


def find_pdf_files(arg_parser: ArgumentParser):
    search_directory = Path(arg_parser.directory)

    if not search_directory.exists():
        raise ValueError(f"Provided directory: {str(search_directory)}\nDoes not exist!")
    
    if arg_parser.recursive:
        return list(search_directory.rglob("*.pdf"))
    return list(search_directory.glob("*.pdf"))



def create_pdf_list(arg_parser: ArgumentParser):

    if arg_parser.directory:
        return find_pdf_files(arg_parser)

    return arg_parser.filenames

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--filenames","-f", action="append", required=False, type = str, default=[],
                        help = "Direct path to file for processing, specify multiple times for multiple files")
    parser.add_argument("--directory","-d", required=False, type=str, default=None,
                        help = "Directory to search for pdf files. Modified with the --recursive [-r] argument.")
    parser.add_argument("--recursive","-r", action="store_true", required=False,
                        help = "Search directory recursively [.rglob]. Default is to just search top level directory [.glob]. Only used with --directory [-d].")
    parser.add_argument("--output","-o", type=str, default = None, required=False,
                        help = "Output filename. Required when using --filenames [-f], defaults to directory provided if using --directory [-d].")

    return parser.parse_args()

def main():

    arg_parser = parse_args()

    assert arg_parser.filenames or arg_parser.directory, (
        "Please provide ONE of --filenames [-f] or --directory [-d] argument")
    

    if arg_parser.filenames:
        assert arg_parser.output is not None, (
            "If providing filename list (--filenames [-f]), you must provide the output filename"
        )

    if arg_parser.output is None:
        output_filename = Path(arg_parser.directory) / "merged.pdf"
        print(f"Ouput file not provided, defaulting to:\n{output_filename}")
    else:
        output_filename = Path(arg_parser.output)

    pdf_list = create_pdf_list(arg_parser=arg_parser)

    merger = PdfWriter()
    for file in pdf_list:
        merger.append(file)


    merger.write(str(output_filename))
    merger.close()



