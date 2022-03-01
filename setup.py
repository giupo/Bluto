from setuptools import setup, find_packages

setup(
    name='bluto',
    version='2.4.20',
    author='Darryl Lane',
    author_email='DarrylLane101@gmail.com',
    url='https://github.com/darryllane/Bluto',
    packages=find_packages(include=["bluto", "bluto.*"]),
    package_data= {
        "bluto": ["bluto/doc/*.txt"]
    },
    include_package_data=True,
    license='LICENSE.txt',
    description='''
    DNS Recon | Brute Forcer | DNS Zone Transfer | DNS Wild Card Checks
    DNS Wild Card Brute Forcer | Email Enumeration | Staff Enumeration
    Compromised Account Checking''',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    install_requires=[
    	"docopt",
        "dnspython",
        "termcolor",
        "BeautifulSoup4",
        "requests[security]",
        "pythonwhois",
        "lxml",
        "oletools",
        "pdfminer",
        "python-whois"
    ],
    entry_points = {
        'console_scripts': [
            'bluto = bluto.cli:main'
        ]
    }
)

