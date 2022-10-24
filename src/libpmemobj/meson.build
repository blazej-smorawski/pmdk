# We use names such as libpmemobj_* because those variables
# are used later on in tests requiring internal files
libpmemobj_sources = files(
    'alloc_class.c',
    'bucket.c',
    'container_ravl.c',
    'container_seglists.c',
    'critnib.c',
    'ctl_debug.c',
    'heap.c',
    'lane.c',
    'libpmemobj.c',
    'list.c',
    'memblock.c',
    'memops.c',
    'obj.c',
    'palloc.c',
    'pmalloc.c',
    'recycler.c',
    'sync.c',
    'tx.c',
    'stats.c',
    'ulog.c',
)

link_args = []

if host_machine.system() == 'linux'
    link_args += '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libpmemobj.link.in')
elif host_machine.system() == 'windows'
    link_args += '-DEF:@0@'.format(meson.current_source_dir() / 'libpmemobj.def')
endif

# Used to build libpmemobj_internal_mocked lib in tests
libpmemobj_dependencies = [
        libdaxctl_dep,
        libndctl_dep,
        libdl_dep,
	    libpmem_dep,
        pmemcommon_dep,
        pmemcore_dep,
        threads_dep,
    ]

libpmemobj_c_args = []

if host_machine.system() == 'linux' and libdl_dep.found()
    libpmemobj_c_args += '-DUSE_LIBDL'
endif

libpmemobj = library(
    'pmemobj',
    libpmemobj_sources,
    c_args: libpmemobj_c_args,
    link_args: link_args,
    dependencies: libpmemobj_dependencies,
    include_directories: root_include,
    name_prefix: 'lib',
    install: true
)

libpmemobj_dep = declare_dependency(
    link_with: libpmemobj,
    include_directories: [
	    root_include,
    ],
)

libpmemobj_internal_include = include_directories('.')

libpmemobj_internal_dep = declare_dependency(
    sources: libpmemobj_sources,
    compile_args: libpmemobj_c_args + [
        '-D_PMEMOBJ_INTRNL',
    ],
    dependencies: [
        libdaxctl_dep,
        libndctl_dep,
	    libdl_dep,
	    libpmem_dep,
        pmemcommon_dep,
        pmemcore_dep,
        threads_dep,
    ],
    include_directories: [
        libpmemobj_internal_include,
        root_include,
    ],
)

if host_machine.system() == 'windows'
    # libpmemobj_internal_dep = declare_dependency(
    #     dependencies: [
    #         libpmemobj_dep
    #     ],
    #     include_directories: [
    #         include_directories('.'),
    #     ]
    # )
endif

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmemobj', libpmemobj_dep)
endif
