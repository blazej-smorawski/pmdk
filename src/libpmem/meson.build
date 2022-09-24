sources = files(
    'libpmem.c',
    '../libpmem2/memops_generic.c',
    'pmem.c',
    'pmem_posix.c',
    '../windows/win_mmap.c',
)

link_args = []

if host_machine.system() == 'linux'
    link_args += '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libpmem.link.in')
elif host_machine.system() == 'windows'
    link_args += '-DEF:@0@'.format(meson.current_source_dir() / 'libpmem.def')
    link_args += ['shlwapi.lib', 'ntdll.lib', 'mincore.lib', 'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib']
endif

libpmem = library(
    'pmem',
    sources,
    link_args: link_args,
    dependencies: [
        libndctl_dep,
        libdaxctl_dep,
        pmemcommon_dep,
        pmemcore_dep,
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
        include_directories('.'),
        root_include,
    ]
)

if host_machine.system() == 'windows'
    libpmem_internal_dep = libpmem_dep
endif

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmem', libpmem_dep)
endif
