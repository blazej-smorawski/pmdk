if host_machine.system() != 'windows'
    sources = files(
        'obj_heap_interrupt.c',
    )

    dependencies = [
        libpmem_dep,
        libpmemobj_internal_dep,
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
        'obj_heap_interrupt.c',
    )

    libpmemobj_memops_object = static_library(
        'memops_object',
        ['../../libpmemobj/memops.c'],
        dependencies: libpmemobj_dependencies + unittest_dep,
        include_directories: [
            libpmemobj_internal_include,
        ],
        c_args: [
            windows_mocks_forced_include,
            '-DWRAP_REAL',
        ],
        install: false,
    )

    libpmemobj_internal_mocked = static_library(
        'pmemobj_mocked',
        [
            '../../libpmemobj/alloc_class.c',
            '../../libpmemobj/bucket.c',
            '../../libpmemobj/container_ravl.c',
            '../../libpmemobj/container_seglists.c',
            '../../libpmemobj/critnib.c',
            '../../libpmemobj/ctl_debug.c',
            '../../libpmemobj/heap.c',
            '../../libpmemobj/lane.c',
            '../../libpmemobj/libpmemobj.c',
            '../../libpmemobj/list.c',
            '../../libpmemobj/memblock.c',
            '../../libpmemobj/obj.c',
            '../../libpmemobj/palloc.c',
            '../../libpmemobj/pmalloc.c',
            '../../libpmemobj/recycler.c',
            '../../libpmemobj/sync.c',
            '../../libpmemobj/tx.c',
            '../../libpmemobj/stats.c',
            '../../libpmemobj/ulog.c',
        ],
        c_args: libpmemobj_c_args + windows_mocks_forced_include,
        dependencies: libpmemobj_dependencies,
        include_directories: [
            root_include,
            libpmemobj_internal_include,
        ],
        objects: [
            libpmemobj_memops_object.extract_objects('../../libpmemobj/memops.c'),
        ],
        name_prefix: 'lib',
    )

    libpmemobj_internal_mocked_dep = declare_dependency(
        link_with: libpmemobj_internal_mocked,
    )

    dependencies = [
        libpmem_dep,
        libpmemobj_internal_mocked_dep,
        unittest_dep,
    ]

    c_args = [
        windows_mocks_forced_include,
        '-DWRAP_REAL',
    ]
    link_args = []
    include_directories = [
        libpmemobj_internal_include,
    ]

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
