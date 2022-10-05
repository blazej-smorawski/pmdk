 # The file has to be compiled as C++ on windows, so
 # it has to be a separate static lib for the purpose
obj_list_object = static_library(
    'obj_list_object',
    ['obj_list.c'],
    dependencies: [
        libpmem_dep,
        unittest_dep,
    ],
    include_directories: [
	    libpmemobj_internal_include,
    ],
    c_args: [
        windows_mocks_forced_include,
        windows_cpp_args,
    ],
    install: false,
)

libpmemobj_lane_object = static_library(
    'libpmemobj_lane_object',
    ['../../libpmemobj/lane.c'],
    dependencies: libpmemobj_dependencies,
    include_directories: [
	    libpmemobj_internal_include,
    ],
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL_LANE'
    ],
    install: false,
)

libpmemobj_pmalloc_object = static_library(
    'libpmemobj_pmalloc_object',
    ['../../libpmemobj/pmalloc.c',
    '../../libpmemobj/palloc.c'],
    dependencies: libpmemobj_dependencies,
    include_directories: [
	    libpmemobj_internal_include,
    ],
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL_PMALLOC'
    ],
    install: false,
)

libpmemobj_ulog_object = static_library(
    'libpmemobj_ulog_object',
    ['../../libpmemobj/ulog.c'],
    dependencies: libpmemobj_dependencies,
    include_directories: [
	    libpmemobj_internal_include,
    ],
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL_ULOG'
    ],
    install: false,
)

libpmemobj_heap_object = static_library(
    'libpmemobj_heap_object',
    ['../../libpmemobj/heap.c'],
    dependencies: libpmemobj_dependencies,
    include_directories: [
	    libpmemobj_internal_include,
    ],
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL_HEAP'
    ],
    install: false,
)

libpmemobj_pmemobj_object = static_library(
    'libpmemobj_pmemobj_object',
    ['../../libpmemobj/obj.c'],
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

libpmemobj_internal_mocked = static_library(
    'pmemobj_mocked',
    [
        '../../libpmemobj/alloc_class.c',
        '../../libpmemobj/bucket.c',
        '../../libpmemobj/container_ravl.c',
        '../../libpmemobj/container_seglists.c',
        '../../libpmemobj/critnib.c',
        '../../libpmemobj/ctl_debug.c',
        '../../libpmemobj/libpmemobj.c',
        '../../libpmemobj/list.c',
        '../../libpmemobj/memblock.c',
        '../../libpmemobj/memops.c',
        '../../libpmemobj/recycler.c',
        '../../libpmemobj/sync.c',
        '../../libpmemobj/tx.c',
        '../../libpmemobj/stats.c',
        '../../libpmemobj/ulog.c',
    ],
    c_args: libpmemobj_c_args,
    dependencies: libpmemobj_dependencies,
    include_directories: [
        root_include,
        libpmemobj_internal_include,
    ],
    objects: [
        libpmemobj_lane_object.extract_objects('../../libpmemobj/lane.c'),
        libpmemobj_pmalloc_object.extract_objects('../../libpmemobj/pmalloc.c'),
        libpmemobj_pmalloc_object.extract_objects('../../libpmemobj/palloc.c'),
        libpmemobj_ulog_object.extract_objects('../../libpmemobj/ulog.c'),
        libpmemobj_heap_object.extract_objects('../../libpmemobj/heap.c'),
        libpmemobj_pmemobj_object.extract_objects('../../libpmemobj/obj.c'),
    ],
    name_prefix: 'lib',
)

libpmemobj_internal_mocked_dep = declare_dependency(
    link_with: libpmemobj_internal_mocked,
)

obj_list_mocks_object = static_library(
    'obj_list_mocks_object',
    ['obj_list_mocks.c'],
    dependencies: libpmemobj_dependencies + unittest_dep,
    include_directories: [
	    libpmemobj_internal_include,
    ],
    c_args: [
        windows_mocks_forced_include,
        '-DWRAP_REAL_ULOG',
        '-DWRAP_REAL_LANE',
        '-DWRAP_REAL_HEAP',
        '-DWRAP_REAL_PMEMOBJ',
    ],
    install: false,
)

obj_list_mocks_palloc_object = static_library(
    'obj_list_mocks_palloc_object',
    ['obj_list_mocks_palloc.c'],
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

sources = files(
    'obj_list.c',
)

dependencies = [
    libpmemobj_dependencies,
    libpmemobj_internal_mocked_dep,
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
    [],
    c_args: c_args,
    link_args: link_args,
    include_directories: [
        include_directories,
        libpmemobj_internal_include,
    ],
    dependencies: dependencies,
    objects: [
        obj_list_object.extract_objects('obj_list.c'),
        obj_list_mocks_object.extract_objects('obj_list_mocks.c'),
        obj_list_mocks_palloc_object.extract_objects('obj_list_mocks_palloc.c'),
    ],
)
