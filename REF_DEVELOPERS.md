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
