from setuptools import setup

long_description = open('README.md').read()

setup(
	name='play-store',
	version='1.0',
	description='Scrapes data from Google Play Store',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/WoolDoughnut310/google-play',
	author='J. Nma',
	author_email='wooldoughnutspi@outlook.com',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries',
		'Programming Language :: Python :: 3'
	],
	keywords='python3 web-scraping google-play data applications',
	py_modules=['play_store'],
	python_requires='>=3'
)