if host_machine.system() != 'windows'
    sources = files(
        'mocks_posix.c',
        'pmem2_granularity.c',
    )


    dependencies = [
        libpmem2_internal_dep,
        unittest_pmem2_dep,
        unittest_dep,
    ]

    c_args = []
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
        'pmem2_granularity.c',
    )

    dependencies = [
        libpmem2_internal_dep,
        unittest_pmem2_dep,
        unittest_dep,
    ]

    c_args = []
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
