#!../env.py
# SPDX-License-Identifier: BSD-3-Clause
# Copyright 2022, Intel Corporation
#
import sys
import testframework as t
from consts import MINIASYNC_LIBDIR
import futils
import re


@t.freebsd_exclude
@t.require_build('debug')
class PMEM2_FUTURE(t.Test):
    test_type = t.Short

    def setup(self, ctx):
        super().setup(ctx)
        if sys.platform == 'win32':
            env_dir = 'PATH'
            pathh = ctx.env[env_dir]
            ctx.env[env_dir] = pathh + ";" + MINIASYNC_LIBDIR
        else:
            env_dir = 'LD_LIBRARY_PATH'
            pathh = ctx.env[env_dir]
            ctx.env[env_dir] = pathh + ":" + MINIASYNC_LIBDIR

    def run(self, ctx):
        file_path = ctx.create_holey_file(16 * t.MiB, 'testfile')
        ctx.env['PMEM2_LOG_LEVEL'] = '15'
        ctx.exec('pmem2_future', self.test_case, file_path, self.size)

        regex = "pmem2_log_flush"

        log_file = self.get_log_file_by_prefix("pmem2")
        log_content = open(log_file).read()
        matches = re.findall(regex, log_content)

        # We expect exactly two matches because first is caused by
        # pmem2_memset_fn call and second should be caused by
        # pmem2_memcpy_async
        if len(matches) != 2:
            futils.fail(F"Failed to find exactly two pmem2_log_flush call! "
                        F"Got {len(matches)} instead.")


class TEST0(PMEM2_FUTURE):
    size = 64
    test_case = 'test_pmem2_future_mover'


class TEST1(PMEM2_FUTURE):
    size = 4096
    test_case = 'test_pmem2_future_mover'


class TEST2(PMEM2_FUTURE):
    size = 64
    test_case = 'test_pmem2_future_vdm'


class TEST3(PMEM2_FUTURE):
    size = 4096
    test_case = 'test_pmem2_future_vdm'
