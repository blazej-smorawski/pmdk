if host_machine.system() != 'windows'
    sources = files(
        'obj_persist_count.c',
    )

    dependencies = [
        libpmem_dep,
        libpmemobj_internal_dep,
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
        'obj_persist_count.c',
    )

    # The sources were copied from obj_persist_cout.vcxproj
    # because the did not match 1:1 into our internal libraries.
    # It's not a good solution, but in order not to break mocking
    # inside those files I decided to do it that way.
    internal_sources = files(
        '../../common/ctl_fallocate.c',
        '../../common/ctl_prefault.c',
        '../../common/ctl_sds.c',
        '../../common/ctl.c',
        '../../common/file_windows.c',
        '../../common/file.c',
        '../../common/mmap_windows.c',
        '../../common/mmap.c',
        '../../common/os_deep_windows.c',
        '../../common/pool_hdr.c',
        '../../common/set.c',
        '../../common/shutdown_state.c',
        '../../common/uuid_windows.c',
        '../../common/uuid.c',
        # '../../core/fs_windows.c',
        # '../../core/os_thread_windows.c',
        # '../../core/os_windows.c',
        # '../../core/out.c',
        # '../../core/ravl.c',
        # '../../core/util_windows.c',
        # '../../core/util.c',
        '../../libpmem2/badblocks_none.c',
        # '../../libpmemobj/alloc_class.c',
        # '../../libpmemobj/bucket.c',
        # '../../libpmemobj/container_ravl.c',
        # '../../libpmemobj/container_seglists.c',
        # '../../libpmemobj/critnib.c',
        # '../../libpmemobj/ctl_debug.c',
        # '../../libpmemobj/heap.c',
        # '../../libpmemobj/lane.c',
        # '../../libpmemobj/libpmemobj.c',
        # '../../libpmemobj/list.c',
        # '../../libpmemobj/memblock.c',
        # '../../libpmemobj/memops.c',
        # '../../libpmemobj/obj.c',
        # '../../libpmemobj/palloc.c',
        # '../../libpmemobj/pmalloc.c',
        # '../../libpmemobj/recycler.c',
        # '../../libpmemobj/stats.c',
        # '../../libpmemobj/sync.c',
        # '../../libpmemobj/tx.c',
        # '../../libpmemobj/ulog.c',
    )

    dependencies = [
        libpmem_dep,
        libpmemobj_internal_dep,
        unittest_dep,
    ]

    c_args = [
        windows_mocks_forced_include,
    ]
    link_args = []
    include_directories = []

    executable(
        t,
        sources + internal_sources,
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
