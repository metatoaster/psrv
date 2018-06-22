from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

classifiers = """
Development Status :: 4 - Beta
License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
Operating System :: OS Independent
Programming Language :: JavaScript
Programming Language :: Python
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Utilities
""".strip().splitlines()

package_json = {
    'dependencies': {
    },
}

setup(
    name='psrv',
    version=version,
    description='A simple psutil web front end',
    long_description=(
        open('README.rst').read() + "\n" +
        open('CHANGES.rst').read()
    ),
    classifiers=classifiers,
    keywords='',
    author='Tommy Yu',
    author_email='y@metatoaster.com',
    url='https://github.com/metatoaster/psrv',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=[],
    zip_safe=False,
    install_requires=[
        'gaugesrv',
        'psutil',
    ],
    package_json=package_json,
    extras_require={
        'dev': [
            # due to pip/setuptools bug, this doesn't actually work
            # 'gaugesrv[dev]',
            # instead the full listing must be manually included
            'calmjs.dev',
            'aiohttp',
        ],
        'rjs': [
            'calmjs.rjs',
        ],
        'webpack': [
            'calmjs.webpack',
        ],
        'scss': [
            'calmjs.sassy[libsass]',
        ],
    },
    extras_calmjs={
        'node_modules': {
        },
    },
    include_package_data=True,
    python_requires='>=3.4',
    build_calmjs_artifacts=True,
    entry_points={
        'calmjs.module': [
            'psrv = psrv',
        ],
        'calmjs.scss': [
            'psrv = psrv',
        ],
        'calmjs.artifacts': [
            'webpack.js = calmjs.webpack.artifact:complete_webpack',
            'styles.css = calmjs.sassy.artifact:complete_css',
        ],
        'console_scripts': [
            'psrv-demo = psrv.app:main',
        ],
    },
    test_suite="psrv.tests.make_suite",
)
