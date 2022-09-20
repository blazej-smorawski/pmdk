include_directories = [
    include_directories('../'),
    include_directories('.'),
]

cpp_args = [] # Args for examples that are compiled as C++ on windows
if host_machine.system() == 'windows'
    cpp_args += '-TP'
endif

executable(
    'btree',
    'btree.c',
    dependencies: [libpmemobj_dep],
    include_directories: include_directories,
    c_args: cpp_args,
)

executable(
    'buffons_needle_problem',
    'buffons_needle_problem.c',
    dependencies: [libpmemobj_dep, libm_dep],
    include_directories: include_directories,
    c_args: cpp_args,
)

executable(
    'lists',
    'lists.c',
    dependencies: [libpmemobj_dep],
    include_directories: include_directories,
    c_args: cpp_args,
)

executable(
    'manpage',
    'manpage.c',
    dependencies: [libpmemobj_dep],
    include_directories: include_directories,
)

executable(
    'pi',
    'pi.c',
    dependencies: [libpmemobj_dep, libm_dep, threads_dep],
    include_directories: include_directories,
    c_args: cpp_args,
)

subdir('hashmap')
subdir('linkedlist')
subdir('list_map')
subdir('tree_map')
subdir('map')
subdir('pmemblk')
subdir('pmemlog')
subdir('pmemobjfs')
subdir('string_store_tx_type')
subdir('string_store_tx')
subdir('string_store')

if host_machine.system() != 'windows'
    executable(
        'setjmp',
        'setjmp.c',
        c_args: '-O2',
        dependencies: [libpmemobj_dep],
        include_directories: include_directories,
    )


    subdir('libart')
    subdir('pminvaders')
    subdir('queue')
    subdir('slab_allocator')
endif
