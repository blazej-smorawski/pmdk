sources = files(
    'badblock.c',
    'config.c',
    'errormsg.c',
    'file.c',
    'libpmemset.c',
    'map_config.c',
    'part.c',
    'pmemset.c',
    'pmemset_utils.c',
    'sds.c',
    'source.c'
)

if host_machine.system() == 'linux'
    sources += files(
        'file_posix.c',
    )
elif host_machine.system() == 'windows'
    sources += files(
        'file_windows.c'
    )
endif

link_args = []

if host_machine.system() == 'linux'
    link_args += '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libpmemset.link.in')
elif host_machine.system() == 'windows'
    link_args += '-DEF:@0@'.format(meson.current_source_dir() / 'libpmemset.def')
    link_args += ['shlwapi.lib', 'ntdll.lib', 'mincore.lib', 'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib']
endif

libpmemset = library(
    'pmemset',
    sources,
    link_args: link_args,
    dependencies: [
        libpmem2_dep,
        pmemcore_dep,
        threads_dep,
    ],
    include_directories: [
        common_include,
        root_include,
    ],
    name_prefix: 'lib',
    install: true,
)

libpmemset_dep = declare_dependency(
    link_with: libpmemset,
    include_directories: root_include,
)

libpmemset_internal_dep = declare_dependency(
    sources: sources,
    dependencies: [
        libpmem2_dep,
        pmemcore_dep,
        threads_dep,
    ],
    include_directories: [
        include_directories('.'),
        common_include,
        root_include,
    ],
)

if meson.version().version_compare('>=0.54')
    meson.override_dependency('libpmemset', libpmemset_dep)
endif
