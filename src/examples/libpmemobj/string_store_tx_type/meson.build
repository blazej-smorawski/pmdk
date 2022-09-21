executable(
    'writer',
    'writer.c',
    dependencies: [libpmemobj_dep, libpmem_dep, threads_dep],
    include_directories: include_directories('.'),
    c_args: windows_cpp_args,
)

executable(
    'reader',
    'reader.c',
    dependencies: [libpmemobj_dep, libpmem_dep, threads_dep],
    include_directories: include_directories('.'),
    c_args: windows_cpp_args,
)
