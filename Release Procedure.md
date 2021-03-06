# Checklist for new release

1. Run unittests: `python runtests.py` or `python setup.py test`
2. Update CHANGELOG.txt
3. Update version in setup.py
4. Push all changes to github
5. Test installation on a different machine in a fresh virtual environment
```bash
cd /tmp
git clone https://github.com/Baguage/django-google-analytics-id
mkvirtualenv analytics
cd django-google-analytics-id
pip install django==1.10
python setup.py test
python setup.py install
deactivate
rmvirtualenv analytics
cd ..
rm -rf django-google-analytics-id
```
6. Make a release/tag

https://github.com/Baguage/django-google-analytics-id/releases -> Draft a new release

Use v0.6.2 format for tag name

7. Run `setup.py sdist bdist_egg bdist_wininst upload` command