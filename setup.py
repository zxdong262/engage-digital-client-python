import setuptools
import json

version = '0.1.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("ringcentral_engage_digital/version", "w") as v:
    v.write(version)

setuptools.setup(
    name="ringcentral_engage_digital",
    version=version,
    author="Drake Zhao @ RingCentral",
    author_email="drake.zhao@ringcentral.com",
    description="RingCentral Engage Digital client Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ringcentral/engage-digital-client-python",
    packages=setuptools.find_packages(),
    keywords=['RingCentral', 'Engage Digital', 'sdk'],
    install_requires=[i.strip() for i in open('requirements.txt').readlines()],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)