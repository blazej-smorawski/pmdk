sources = files(
    'alloc.c',
    'membuf.c',
    'out.c',
    'ravl.c',
    'ravl_interval.c',
    'util.c',
)

if host_machine.system() == 'linux'
    sources += files(
        'fs_posix.c',
        'os_posix.c',
        'os_thread_posix.c',
        'util_posix.c'
    )
elif host_machine.system() == 'windows'
    sources += files(
        'fs_windows.c',
        'os_windows.c',
        'os_thread_windows.c',
        'util_windows.c',
    )
endif

pmemcore_dep = declare_dependency(
    sources: sources,
    dependencies: [
	    threads_dep,
    ],
    include_directories: [
	    include_directories('.'),
        common_include,
        windows_include,
    ],
)
