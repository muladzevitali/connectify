import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="connectify",
    version="0.1.2",
    author="Vitali Muladze",
    author_email="muladzevitali@gmail.com",
    description="Different Python I/O handlers",
    long_description=long_description,
    install_requires=install_requires,
    long_description_content_type="text/markdown",
    url="https://github.com/muladzevitali/connectify",
    project_urls={
        "Bug Tracker": "https://github.com/muladzevitali/connectify/issuesL",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=("connectify",
              "connectify.slack_services"
              ),
    python_requires=">=3.8"
)
