if host_machine.system() != 'windows'
    sources = files(
        'obj_memblock.c',
    )

    dependencies = [
        libpmemobj_internal_dep,
        unittest_dep,
    ]

    c_args = [
        #'-FI@0@\src\windows\include\mocks_windows.h'.format(meson.project_source_root()),
        windows_mocks_forced_include,
    ]
    link_args = []
    include_directories = [
        windows_include
    ]

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
        'obj_memblock.c',
    )

    libpmemobj_memops_object = static_library(
        'libpmemobj_memops_object',
        ['../../libpmemobj/memops.c'],
        dependencies: libpmemobj_dependencies,
        include_directories: [
            libpmemobj_internal_include,
            root_include,
        ],
        c_args: [
            windows_mocks_forced_include,
            '-DWRAP_REAL'
        ],
        install: false,
    )   

    # Remove memops.c from libpmemobj_sources for mocked libpmemobj
    # because the file was built above in the libpmemobj_memops_object
    libpmemobj_internal_mocked_sources = [
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
    ]
    # foreach file : libpmemobj_sources
    #     if file not in files('../../libpmemobj/memops.c')
    #         #libpmemobj_internal_mocked_sources += file
    #         message(file)
    #     else
    #         message(file)
    #     endif
    # endforeach

    libpmemobj_internal_mocked = static_library(
        'pmemobj_mocked',
        libpmemobj_internal_mocked_sources,
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
        libpmemobj_internal_mocked_dep,
        unittest_dep,
    ]

    c_args = [
        windows_mocks_forced_include,
    ]
    link_args = []
    include_directories = [
        libpmemobj_internal_include,
        windows_include
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
