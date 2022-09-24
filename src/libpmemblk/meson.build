sources = files(
    'blk.c',
    'btt.c',
    'libpmemblk.c'
)

link_args = []

if host_machine.system() == 'linux'
    link_args += '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libpmemblk.link.in')
elif host_machine.system() == 'windows'
    link_args += '-DEF:@0@'.format(meson.current_source_dir() / 'libpmemblk.def')
    link_args += ['shlwapi.lib', 'ntdll.lib', 'mincore.lib', 'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib']
endif

libpmemblk = library(
    'pmemblk',
    sources,
    link_args: link_args,
    dependencies: [
        libdaxctl_dep,
        libndctl_dep,
        libpmem_dep,
        pmemcommon_dep,
        pmemcore_dep,
        threads_dep,
    ],
    include_directories: root_include,
    name_prefix: 'lib',
    install: true
)

libpmemblk_dep = declare_dependency(
    link_with: libpmemblk,
    include_directories: root_include,
)

libpmemblk_internal_dep = declare_dependency(
    sources: sources,
    dependencies: [
        libdaxctl_dep,
        libndctl_dep,
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
    libpmemblk_internal_dep = libpmemblk_dep
endif

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmemblk', libpmemblk_dep)
endif
