sources = files(
    'libpmempool.c',
    'check.c',
    'check_bad_blocks.c',
    'check_backup.c',
    'check_btt_info.c',
    'check_btt_map_flog.c',
    'check_log.c',
    'check_blk.c',
    'check_pool_hdr.c',
    'check_sds.c',
    'check_util.c',
    'check_write.c',
    'pool.c',
    'replica.c',
    'feature.c',
    'sync.c',
    'transform.c',
    'rm.c'
)

link_args = []

if host_machine.system() == 'linux'
    link_args += '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libpmempool.link.in')
elif host_machine.system() == 'windows'
    link_args += '-DEF:@0@'.format(meson.current_source_dir() / 'libpmempool.def')
endif

dependencies = [
        libdaxctl_dep,
        libndctl_dep,
        libpmem_dep,
        pmemcommon_dep,
        pmemcore_dep,
        threads_dep,
    ]
    
if host_machine.system() == 'linux'
    dependencies += libdl_dep
endif

c_args = []

if host_machine.system() == 'linux'
    c_args += '-DUSE_LIBDL'
endif

libpmempool = library(
    'pmempool',
    sources,
    objects: libpmemblk.extract_objects('btt.c'),
    c_args: c_args,
    link_args: link_args,
    dependencies: dependencies,
    include_directories: [
        include_directories('../libpmemlog'),
        include_directories('../libpmemblk'),
        include_directories('../libpmemobj'),
        include_directories('../libpmem2'),
        root_include,
        windows_include,
    ],
    name_prefix: 'lib',
    install: true
)

libpmempool_dep = declare_dependency(
    link_with: libpmempool,
    include_directories: root_include,
)

libpmempool_internal_dep = declare_dependency(
    sources: sources,
    compile_args: c_args,
    dependencies: dependencies,
    include_directories: [
        include_directories('.'),
        include_directories('../windows/include'),
        root_include,
        windows_include,
    ],
)

if host_machine.system() == 'windows'
    libpmempool_internal_dep = libpmempool_dep
endif

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmempool', libpmempool_dep)
endif
