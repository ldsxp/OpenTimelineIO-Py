from setuptools import setup

"""
This is an example of how to an OpenTimelineIO plugin installable as a separate
python package.

For the most part, the module can be built like any other python module, the
one exception is that it must expose an ``opentimelineio_py.plugins`` entry point
to allow OTIO to discover it.

The entry point defined below can be read as:
    1. Declaring this module provides for the entry point group
    ``opentimelineio_py.plugins``.
    2. Declaring that for the ``opentimelineio_py.plugins`` group, this module
    provides a plugin named ``track_counter`` and the module that should be
    loaded for tha plugin is the ``otio_counter`` module.

For more information about python plugins, see the python packaging guide:
    https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata
"""

setup(
    name='otio_counter',
    entry_points={
        'opentimelineio_py.plugins': 'track_counter = otio_counter'
    },
    packages=['otio_counter'],
    package_data={
        'otio_counter': [
            'plugin_manifest.json',
        ],
    },
    keywords='plugin opentimelineio_py sample',
    platforms='any',
    version='1.0.0',
    description='Adapter writes number of tracks to file.',
    license='Modified Apache 2.0 License',
    author='Pixar Animation Studios',
    author_email='opentimelineio@pixar.com',
    url='http://opentimeline.io',
)
