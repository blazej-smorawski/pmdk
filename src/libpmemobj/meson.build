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
    link_args += ['shlwapi.lib', 'ntdll.lib', 'mincore.lib', 'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib']
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
	#    libdl_dep,
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

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmemobj', libpmemblk_dep)
endif
