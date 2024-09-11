# to update the book -

cd /home/breezy/Documents/GitHub/University-Subjects

jupyter-book build Time-Variants-Authority

or rebuild with

jupyter-book build --all Time-Variants-Authority

## to push the book to GitHub Pages -

cd /home/breezy/Documents/GitHub/Jupyter-Books/Time-Variants-Authority

make sure in main -

ghp-import -n -p -f _build/html

