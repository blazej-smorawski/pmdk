
dependencies = [
        libndctl_dep,
        libdaxctl_dep,
        libpmem_dep,
        libpmemblk_dep,
        libpmemlog_dep,
        libpmemobj_dep,
        libpmempool_dep,
        pmemcore_dep,
        pmemcommon_dep,
        threads_dep
    ]

if host_machine.system() == 'windows'
    dependencies += getopt_dep
endif

pmempool = executable(
    'pmempool',
    sources: files(
            'pmempool/check.c',
            'pmempool/common.c',
            'pmempool/convert.c',
            'pmempool/create.c',
            'pmempool/dump.c',
            'pmempool/feature.c',
            'pmempool/info_blk.c',
            'pmempool/info_log.c',
            'pmempool/info_obj.c',
            'pmempool/info.c',
            'pmempool/output.c',
            'pmempool/pmempool.c',
            'pmempool/rm.c',
            'pmempool/synchronize.c',
            'pmempool/transform.c',
        ),
    objects: [
            libpmemblk.extract_objects('btt.c'),
            libpmemobj.extract_objects('alloc_class.c', 'bucket.c', 'container_ravl.c', 'container_seglists.c', 'critnib.c', 'heap.c', 'memblock.c', 'memops.c', 'recycler.c', 'ulog.c'),
        ],
    include_directories: [
            root_include,
            windows_include,
            include_directories('../libpmemblk'),
            include_directories('../libpmemlog'),
            include_directories('../libpmemobj'),
        ],
    dependencies: dependencies,
    install: true
)

if host_machine.system() != 'windows'
    executable(
        'daxio',
        sources: files('daxio/daxio.c'),
        include_directories: [
                core_include,
                common_include,
                root_include,
            ],
        dependencies: [
                libpmem_dep,
                libndctl_dep,
                libdaxctl_dep,
                pmemcore_dep,
                pmemcommon_dep,
            ],
        install: true,
    )


    if get_option('rpmem')
        rpmemd = executable(
            'rpmemd',
            c_args: ['-DRPMEMC_LOG_RPMEMD'],
            sources: files(
                    'rpmemd/rpmemd.c',
                    'rpmemd/rpmemd_log.c',
                    'rpmemd/rpmemd_config.c',
                    '../rpmem_common/rpmem_common.c',
                    'rpmemd/rpmemd_obc.c',
                    'rpmemd/rpmemd_db.c',
                    'rpmemd/rpmemd_fip.c',
                    '../rpmem_common/rpmem_fip_common.c',
                    'rpmemd/rpmemd_util.c'
                ),
            dependencies: [
                    libfabric_dep,
                    libpmem_dep,
                    pmemcore_dep,
                    pmemcommon_dep,
                    threads_dep,
                ],
            include_directories: [
                    include_directories('rpmemd'),
                    core_include,
                    common_include,
                    root_include,
                    include_directories('../rpmem_common'),
                ],
            install: true
        )
    endif

    rpmemd_dep = declare_dependency(
        sources: files(
            'rpmemd/rpmemd_log.c',
            'rpmemd/rpmemd_config.c',
            'rpmemd/rpmemd_obc.c',
            'rpmemd/rpmemd_db.c',
            'rpmemd/rpmemd_fip.c',
            'rpmemd/rpmemd_util.c',
        ),
        dependencies: libfabric_dep,
        include_directories: [
            include_directories('rpmemd'),
        include_directories('../rpmem_common'),
        ],
    )
endif
