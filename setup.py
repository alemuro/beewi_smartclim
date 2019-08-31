import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beewi_smartclim",
    version="0.0.6",
    author="alemuro",
    author_email="hola@aleixmurtra.com",
    description="Library to read data from BeeWi SmartClim sensor using Bluetooth LE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alemuro/beewi_smartclim",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['btlewrap==0.0.2', 'bluepy'],
    keywords='temperature and humidity sensor bluetooth low-energy ble beewi smartclim',
)