# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


requires = []
dep_links = []

for dep in open('requirements.txt').read().split("\n"):
    if dep.startswith('git+'):
        dep_links.append(dep)
    else:
        requires.append(dep)


setup(
    name="django-debugmail",
    version="1.0.4",
    description="Debug based e-mail backend.",
    author=u"James Cleveland",
    author_email="jc@blackflags.co.uk",
    url="https://github.com/radiosilence/django-debugmail.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    dependency_links=dep_links,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        ],
    zip_safe=False,
)
