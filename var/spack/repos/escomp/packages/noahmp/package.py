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
#     spack install noahmp
#
# You can edit this file again by typing:
#
#     spack edit noahmp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

#from git import Repo
import os
import subprocess
from spack import *
from spack.util.executable import Executable


class Noahmp(CMakePackage):
    """Noah-MP is a community land model contributed by the whole Noah-MP 
    scientific community."""

    homepage = "https://github.com/uturuncoglu/noahmp"
    url      = "https://github.com/NOAA-EMC/noahmp/archive/refs/tags/v3.8.tar.gz"
    git      = "https://github.com/uturuncoglu/noahmp.git"

    maintainers = ['uturuncoglu']

    #version('develop', branch='feature/nuopc_cap')
    #version('d8136d6', commit='d8136d651cd15ddb1f0fc1e3e298e498369f41c2') 

    # list refs/heads and refs/tags and add them as version
    git_exe = which('git', required=True)
    cmd = '{} ls-remote --refs {}'.format(git_exe, git)
    git_lst = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE).stdout.splitlines()

    # loop over list and define them as version
    for item in git_lst:
        # split item as hash, branch/tag name
        item_lst = list(item.split('\t'))

        # replace / with _ in version name since spack does not good with / in the version string
        _name = item_lst[1]
        refs_name = _name.replace('refs/heads/', '')
        refs_name = refs_name.replace('refs/tags/', '')
        version_name = refs_name.replace('/', '_')

        # skip some common branches
        if 'gh-pages' in _name:
            continue

        # add tags and branches to the version
        if 'refs/tags' in _name:
            version(version_name, tag=refs_name)
        elif 'refs/heads' in _name:
            version(version_name, branch=refs_name)

    depends_on('mpi')
    depends_on('netcdf-c', type='link')
    depends_on('netcdf-fortran', type='link')
    depends_on('esmf', type='link')
    depends_on('fms', type='link')

    def cmake_args(self):
        define = self.define
        spec = self.spec
        args = []

        return args

    #@run_after('install')
    #def set_versions(self):
    #    spec = self.spec
    #    git_exe = Executable(spec['git'].prefix.bin + "/git")
    #    print(git_exe)

    def pre_build(self):
        spec = self.spec
        if "jit=impalajit" in spec:
            impalajir_src = join_path(self.stage.source_path, 'impalajit')
            if os.path.isdir(impalajir_src):
                shutil.rmtree(impalajir_src)

            git_exe = GitExe()
            git_exe('clone', 'https://github.com/uphoffc/ImpalaJIT.git', impalajir_src)
            with working_dir(join_path(impalajir_src, 'build'), create=True):
                cmake('..', '-DCMAKE_INSTALL_PREFIX={0}'.format(self.spec.prefix))
                make()
                make('install')
