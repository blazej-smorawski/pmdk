sources = files(
    'libpmem.c',
    '../libpmem2/memops_generic.c',
    'pmem.c',
)

link_args = []

if host_machine.system() == 'linux'
    link_args += '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libpmem.link.in')
    sources += 'pmem_posix.c'
elif host_machine.system() == 'windows'
    link_args += '-DEF:@0@'.format(meson.current_source_dir() / 'libpmem.def')
    sources += ['pmem_windows.c', '../windows/win_mmap.c']
endif

libpmem_include = [
    include_directories('.'),
    root_include,
]

libpmem = library(
    'pmem',
    sources,
    link_args: link_args,
    dependencies: [
        libndctl_dep,
        libdaxctl_dep,
        pmemcommon_dep,
        pmemcore_dep, # pmemcore is included in pmemcommon_dep
        pmem2arch_dep,
    ],
    include_directories: [
        root_include,
    ],
    name_prefix: 'lib',
    install: true,
)

libpmem_dep = declare_dependency(
    link_with: libpmem,
    include_directories: root_include,
)

libpmem_internal_dep = declare_dependency(
    sources: sources,
    dependencies: [
        libndctl_dep,
        libdaxctl_dep,
        pmemcommon_dep,
        pmemcore_dep,
        pmem2arch_dep,
    ],
    include_directories: [
        libpmem_include,
    ]
)

if host_machine.system() == 'windows'
    #libpmem_internal_dep = libpmem_dep
endif

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmem', libpmem_dep)
endif
