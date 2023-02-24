How to reproduce:

```shell
pip install -r requirements-test.txt
pip-extra-reqs -d src  # works
tox  # doesn't work
```