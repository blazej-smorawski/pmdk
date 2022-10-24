mocks_windows_object = static_library(
    'mocks_windows_object',
    ['mocks_windows.c'],
    dependencies: unittest_dep,
    include_directories: [],
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL',
    ],
    install: false,
)

libpmem2_init_object = static_library(
    'libpmem2_init_object',
    ['../../libpmem2/x86_64/init.c'],
    dependencies: [
        pmemcommon_dep,
        unittest_dep,
    ],
    include_directories: include_directories(
        '../../libpmem',
        '../../libpmem2',
        '../../libpmem2/x86_64'
    ),
    c_args: [
        windows_mocks_forced_include,
        '-DSSE2_AVAILABLE=0',
        '-DAVX_AVAILABLE=0',
        '-DAVX512F_AVAILABLE=0',
    ],
    install: false,
)

# The sources were copied from pmem_map_file_win.vcxproj
# because the did not match 1:1 into our internal libraries.
# It's not a good solution, but in order not to break mocking
# inside those files I decided to do it that way.
internal_sources = files(
    '../../libpmem/pmem.c',
    '../../libpmem/libpmem.c',
    '../../libpmem2/memops_generic.c',
    '../../libpmem2/x86_64/cpu.c',
    '../../libpmem/pmem_windows.c',
    '../../windows/win_mmap.c',
)

sources = files(
    'pmem_map_file_win.c',
)

dependencies = [
    pmemcommon_dep,
    libdl_dep,
    unittest_dep,
]

c_args = [
    windows_mocks_forced_include
]
link_args = []
include_directories = [
    libpmem2_arch_include
]

executable(
    t,
    sources + internal_sources,
    c_args: c_args,
    link_args: link_args,
    include_directories: include_directories,
    dependencies: dependencies,
    objects: [
            mocks_windows_object.extract_objects('mocks_windows.c'),
            libpmem2_init_object.extract_objects('../../libpmem2/x86_64/init.c')
        ],
)

copy_target = custom_target(t+'(test-files)',
    input : test_files,
    output :  test_files,
    command : [copy, '-i', '@INPUT@', '-o', '@OUTPUT@'],
    install : false,
    build_by_default : true
)
