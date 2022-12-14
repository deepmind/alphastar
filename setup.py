# Copyright 2021 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module setuptools script."""

from importlib import util
from setuptools import find_packages
from setuptools import setup


def get_version():
  spec = util.spec_from_file_location('_metadata', 'alphastar/_metadata.py')
  mod = util.module_from_spec(spec)
  spec.loader.exec_module(mod)
  return mod.__version__

with open('requirements.txt') as f:
  required = f.read().splitlines()


LONG_DESCRIPTION = (
    'This package provides libraries for ML-friendly Starcraft II trajectory '
    'data generation, architectures and agents along with the entire training '
    'and evaluation setup for training an offline RL agent.'
)

setup(
    name='AlphaStar',
    version=get_version(),
    description='Package for offline RL agent training and evaluation on StarCraftII',
    long_description=LONG_DESCRIPTION,
    author='DeepMind',
    license='Apache License, Version 2.0',
    keywords='StarCraft AI',
    url='https://github.com/deepmind/alphastar',
    # This is important if you have some non-standard files as part of package.
    include_package_data=True,
    packages=find_packages(),
    # dm-acme 0.2.4 until the clash of pybind11 absl status bindings with
    # PySC2 is resolved.
    install_requires=required,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
