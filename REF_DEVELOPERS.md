# REF: Developers

## Development: Manage Environment

Use the professional Python workflow described in [pro-analytics-01](https://github.com/denisecase/pro-analytics-01)

```shell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
```

## Development: Open Notebook

Open the notebook main.ipynb in VS Code. Set notebook kernel to Python Environment and select the local .venv virtual environment. Run all. 

## Development: Before Changes

Pull and activate the .venv if not already active.

```shell
git pull
.\.venv\Scripts\activate
```

## Development: After Changes

Git add, commit, and push changes to GitHub repo.

```shell
git add .
git commit -m "did this"
git push -u origin main
```

## Publishing Interactive Notebooks with Voilà

This project uses Voilà to publish notebooks using interactive widgets (e.g., drop-downs). 

**Try it on Binder**:  
[![Open in Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/denisecase/mn-gis-boundaries/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fmain.ipynb)

### To run Voilà locally

From the project root, run the following command to launch a notebook as a standalone interactive web app.

```bash
voila main.ipynb
```

### Development Notes

To publish with Voilà, add `notebook` and `voila` packages to requirements.txt.
This may affect how charts are rendered during development especially in VS Code. 
For example, maps and charts may appear multiple times in VS Code notebooks after these two packages are installed.
