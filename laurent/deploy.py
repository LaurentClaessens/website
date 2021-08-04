#!venv/bin/python3

from pathlib import Path
import subprocess
import shutil

import dirmanage


dprint = print

REMOTE = "claessenvs@ftp.cluster003.hosting.ovh.net"


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


def fill_builds():
    """Make markdown -> html and copy the html files to `builds`."""
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


def create_batchfile():
    skel = open("batchfile.skel", 'r').read()
    put_html_list = []
    for filename in dirmanage.builds_dir.iterdir():
        put_html_list.append(f"put {filename}")

    put_html = "\n".join(put_html_list)
    text = skel.replace("__PUT_HTML__", put_html)

    batch_filename = "batchfile"
    with open(batch_filename, 'w') as batchfile:
        batchfile.write(text)
        print(f"save: {batch_filename}")


def copy_ovh():
    """Send the whole to ovh."""
    subprocess.call(['sftp', '-b', 'batchfile', REMOTE])


def do_work():
    """Do the work."""
    fill_builds()
    create_batchfile()
    copy_ovh()


do_work()
