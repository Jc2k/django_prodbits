from setuptools import setup, find_packages

version = '0.0.0.dev0'

setup(
    name='django_prodbits',
    version=version,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points = """
    [console_scripts]
    django = prodbits.scripts.django:main
    """
    )

