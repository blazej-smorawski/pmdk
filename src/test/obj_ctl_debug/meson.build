sources = files(
    'obj_ctl_debug.c',
)

dependencies = [
    libpmemobj_dep,
    unittest_dep,
]
# TODO: Check if it should be used because it's not in 
# Visual Studio solution
c_args = []
include_directories = []

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
