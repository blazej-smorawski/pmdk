if host_machine.system() != 'windows'
    sources = files(
        'obj_sds.c',
    )

    dependencies = [
        libpmemobj_internal_dep,
        libpmempool_dep,
        unittest_dep,
    ]

    c_args = [
        windows_mocks_forced_include,
    ]
    link_args = []
    include_directories = []

    # scan test source files for mock functions
    ret = run_command(
            get_mocks,
            sources,
            check: true,
    )

    mock_funcs = ret.stdout().strip().split('\n')
    if mock_funcs.length() != 0
        wrap_arg_str = '-Wl'
        foreach mock : mock_funcs
            wrap_arg_str += f',--wrap=@mock@'
        endforeach
        link_args += [wrap_arg_str]
    endif

    executable(
        t,
        sources,
        c_args: c_args,
        link_args: link_args,
        include_directories: include_directories,
        dependencies: dependencies,
    )
else
    sources = files(
        'obj_sds.c',
    )

    # It's not using libpmemobj_internal_dep because it requires pmemcommon_internal_dep
    libpmemobj_internal_mocked = static_library(
        'pmemobj_mocked',
        libpmemobj_sources,
        c_args: libpmemobj_c_args + windows_mocks_forced_include,
        dependencies: [
            libdaxctl_dep,
            libndctl_dep,
            libdl_dep,
            libpmem_dep,
            pmemcommon_internal_dep,
            pmemcore_dep,
            threads_dep,
            miniasync_dep,
        ],
        include_directories: [
            root_include,
            libpmemobj_internal_include,
        ],
        objects: [],
        name_prefix: 'lib',
    )

    libpmemobj_internal_mocked_dep = declare_dependency(
        link_with: libpmemobj_internal_mocked,
    )

    dependencies = [
        libpmemobj_internal_mocked_dep,
        libpmempool_dep,
        unittest_dep,
    ]

    c_args = [
        windows_mocks_forced_include,
        '-DWRAP_REAL',
    ]
    link_args = []
    include_directories = []

    executable(
        t,
        sources,
        c_args: c_args,
        link_args: link_args,
        include_directories: include_directories,
        dependencies: dependencies,
    )
endif

copy_target = custom_target(t+'(test-files)',
    input : test_files,
    output :  test_files,
    command : [copy, '-i', '@INPUT@', '-o', '@OUTPUT@'],
    install : false,
    build_by_default : true
)