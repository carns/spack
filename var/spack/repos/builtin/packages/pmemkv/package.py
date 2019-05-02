# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pmemkv(CMakePackage):
    """Key/Value Datastore for Persistent Memory"""

    homepage = "https://github.com/pmem/pmemkv"
    git      = "https://github.com/pmem/pmemkv.git"

    version('master', git='https://github.com/pmem/pmemkv.git')

    # pmemkv has no tagged releases as of May 1, 2019
    version('develop', branch='master')

    depends_on('libpmemobj-cpp')
    depends_on('memkind')
    depends_on('rapidjson')
    depends_on('intel-tbb')

    def install(self, spec, prefix):
        make("install", "prefix=%s" % prefix)
