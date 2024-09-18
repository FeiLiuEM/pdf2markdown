# pdf2markdown

A tool which can transfer pdf to markdown file. This project is based on [e2m](https://github.com/wisupai/e2m).



## How to use it

### Install the environment

```bash
# create environment
conda create -n e2m python=3.10
conda activate e2m

# update pip
pip install --upgrade pip

# install e2m
# Option 1: Install via git, most recommended
pip install git+https://github.com/wisupai/e2m.git --index-url https://pypi.org/simple
# Option 2: Install via pip
pip install --upgrade wisup_e2m
# Option 3: Manual installation
git clone https://github.com/wisupai/e2m.git
cd e2m
pip install poetry
poetry build
pip install dist/wisup_e2m-0.1.63-py3-none-any.whl
```

### Then copy your pdf file to `pdf` folder. 

### Run python script

`conda activate e2m`

`python  pdf_2_markdown.py`

You will get the `md` file in the `markdown` folder.