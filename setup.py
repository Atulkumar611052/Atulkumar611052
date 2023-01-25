import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description= f.read()

__version__="0.0.0"

REPO_NAME="template-setup-1.0"
AUTHOR_USER_NAME= "C17hawke"
SRC_REPO="template-setup-1.0"
AUTHOR_EMAIL="anamikagolu1508@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_mail=AUTHOR_EMAIL,
    author_user_name=AUTHOR_USER_NAME,
    description="A small python package",
    long_description=long_description,
    long_description="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug tracker":f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"scr"},
    packages=setuptools.find_packages(where="src")
)
