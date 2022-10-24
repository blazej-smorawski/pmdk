sources = files(
    'pmem_has_auto_flush_win.c',
)

dependencies = [
    unittest_dep,
    pmemcommon_dep,
]

c_args = [
    windows_mocks_forced_include,
    '-DSSE2_AVAILABLE=0',
    '-DAVX_AVAILABLE=0',
    '-DAVX512F_AVAILABLE=0',
]
link_args = []
include_directories = [
    libpmem_include,
    libpmem2_include,
    include_directories('.'),
]

mocks_windows_object = static_library(
    'mocks_windows_object',
    ['mocks_windows.c'],
    dependencies: unittest_dep,
    include_directories: include_directories,
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL',
        '-D_DEBUG',
        '-D_CONSOLE',
    ],
    install: false,
)

# The sources were copied from pmem_has_auto_flush_win.vcxproj
# because the did not match 1:1 into our internal libraries.
# It's not a good solution, but in order not to break mocking
# inside those files I decided to do it that way.
internal_sources = files(
    '../../common/file.c',
    '../../libpmem/pmem_windows.c',
    '../../libpmem/pmem.c',
    '../../libpmem2/auto_flush_windows.c',
    '../../libpmem2/memops_generic.c',
    '../../libpmem2/x86_64/cpu.c',
    '../../libpmem2/x86_64/init.c',
    '../../windows/win_mmap.c',
)

executable(
    t,
    sources + internal_sources,
    c_args: c_args,
    link_args: link_args,
    include_directories: include_directories,
    dependencies: dependencies,
    objects: mocks_windows_object.extract_objects('mocks_windows.c'),
)

copy_target = custom_target(t+'(test-files)',
    input : test_files,
    output :  test_files,
    command : [copy, '-i', '@INPUT@', '-o', '@OUTPUT@'],
    install : false,
    build_by_default : true
)