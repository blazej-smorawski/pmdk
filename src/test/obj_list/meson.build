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
        windows_mock_forced_include,
        windows_cpp_args,
    ],
    install: false,
)

libpmemobj_lane_object = static_library(
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
        windows_mock_forced_include,
        windows_cpp_args,
    ],
    install: false,
)

sources = files(
    'obj_list_mocks_palloc.c',
    'obj_list_mocks.c',
)

dependencies = [
    libpmem_dep,
    libpmemobj_internal_dep,
    unittest_dep,
]

c_args = [
    windows_mock_forced_include,
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
    objects: obj_list_object.extract_objects('obj_list.c')
)
