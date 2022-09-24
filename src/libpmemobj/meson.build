sources = files(
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

dependencies = [
        libdaxctl_dep,
        libndctl_dep,
	    libpmem_dep,
        pmemcommon_dep,
        pmemcore_dep,
        threads_dep,
    ]
    
if host_machine.system() == 'linux' and libdl_dep.found()
    dependencies += libdl_dep
endif

c_args = []

if host_machine.system() == 'linux' and libdl_dep.found()
    c_args += '-DUSE_LIBDL'
endif

libpmemobj = library(
    'pmemobj',
    sources,
    c_args: c_args,
    link_args: link_args,
    dependencies: dependencies,
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

libpmemobj_internal_dep = declare_dependency(
    sources: sources,
    compile_args: [
        '-DUSE_LIBDL',
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
        include_directories('.'),
        root_include,
    ],
)

if host_machine.system() == 'windows'
    libpmemobj_internal_dep = declare_dependency(
        dependencies: [
            libpmemobj_dep
        ],
        include_directories: [
            include_directories('.'),
        ]
    )
endif

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmemobj', libpmemobj_dep)
endif
