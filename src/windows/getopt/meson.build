if host_machine.system() == 'windows'
    getopt = static_library(
        'getopt',
        'getopt.c',
        include_directories: include_directories('.'),
        install: false,
    )

    getopt_dep = declare_dependency(
        link_with: getopt,
        include_directories: include_directories('.'),
    )
else
    # Empty dependency for tests that need getop on windows
    getopt_dep = declare_dependency()
endif