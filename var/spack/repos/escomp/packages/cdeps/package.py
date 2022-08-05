# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cdeps
#
# You can edit this file again by typing:
#
#     spack edit cdeps
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Cdeps(CMakePackage):
    """The Community Data Models for Earth Predictive Systems (CDEPS) contains 
    a set of NUOPC-compliant data components along with ESMF-based share code 
    that enables new capabilities in selectively removing feedbacks in coupled 
    model systems."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://escomp.github.io/CDEPS/html/index.html"
    url      = "https://github.com/ESCOMP/CDEPS/archive/refs/tags/cdeps0.12.54.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.12.54', sha256='70025257c24068b806670cfc908117d300d4982426e22a1490448d630ab77753')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
