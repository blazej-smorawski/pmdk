sources = files(
    'getopt.c',
)

dependencies = [
    unittest_dep,
    getopt_dep,
]

c_args = []
include_directories = [
    windows_getopt_include,
]

executable(
    t,
    sources,
    c_args: c_args,
    include_directories: include_directories,
    dependencies: dependencies,
)

copy_target = custom_target(t+'(test-files)',
    input : test_files,
    output :  test_files,
    command : [copy, '-i', '@INPUT@', '-o', '@OUTPUT@'],
    install : false,
    build_by_default : true
)
