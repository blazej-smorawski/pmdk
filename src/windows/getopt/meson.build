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