#!venv/bin/python3

from pathlib import Path
import subprocess
import shutil

import dirmanage


dprint = print


def md_to_body(md_filename):
    """Return the body section of a html code from a markdown file."""
    bytes_ans = subprocess.check_output(
        ['pandoc',
            '--mathml', '-s',
            md_filename])
    html_base = bytes_ans.decode("utf8")
    start_tag = "<body>"
    end_tag = "</body>"
    start = html_base.find(start_tag) + len(start_tag)
    stop = html_base.find(end_tag)
    return html_base[start:stop]


def create_html(md_filename):
    """Create the final html from the given markdown."""
    print(f"build: {md_filename}")
    skel = open("html_page.skel", 'r').read()
    body = md_to_body(md_filename)
    return skel.replace("__BODY_HERE__", body)


def copy_to_build(filename):
    """Copy the give filename to the build directory."""
    dst = dirmanage.builds_dir
    shutil.copy(filename, dst)


def do_work():
    """Do the work."""
    textes_dir = dirmanage.init_dir / "textes"
    for elem in textes_dir.iterdir():
        if elem.suffix == ".html":
            copy_to_build(elem)
            continue

        if elem.suffix == ".md":
            html_code = create_html(elem)
            html_filename = Path(elem.name).with_suffix(".html")
            new_filepath = dirmanage.builds_dir / html_filename
            with open(new_filepath, 'w') as new_file:
                new_file.write(html_code)
            continue


do_work()
