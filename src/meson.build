root_include = include_directories('include')
common_include = include_directories('common')
core_include = include_directories('core')
windows_cpp_args = [] # Args for examples that are compiled as C++ on windows

# The include is added to each source file compiled on windows
if host_machine.system() == 'windows'
    add_project_arguments('-FI@0@\src\windows\include\platform.h'.format(meson.project_source_root()), language : 'c')
    add_project_arguments('-DPMDK_UTF8_API', language: 'c')
    add_project_link_arguments(
        ['shlwapi.lib', 'ntdll.lib', 'mincore.lib', 
        'kernel32.lib', 'user32.lib', 'gdi32.lib', 'winspool.lib', 
        'comdlg32.lib', 'advapi32.lib', 'shell32.lib', 'ole32.lib', 
        'oleaut32.lib', 'uuid.lib', 'odbc32.lib', 'odbccp32.lib']
        , language: 'c'
        )
    windows_include = include_directories('windows/include')
    windows_getopt_include = include_directories('windows/getopt')
    windows_mocks_forced_include = '-FImocks_windows.h'

    if host_machine.system() == 'windows'
        windows_cpp_args += ['-std:c++14', '-TP']
    endif
else
    windows_include = ''
    windows_getopt_include = ''
    windows_mocks_forced_include = ''
endif

subdir('core')
subdir('libpmem2')
subdir('common')
subdir('libpmem')
subdir('libpmemblk')
subdir('libpmemlog')
subdir('libpmemobj')
subdir('libpmempool')
subdir('libpmemset')
subdir('examples')
subdir('windows') # Provides getop_dep for tests


if get_option('rpmem')
    #subdir('librpmem')
endif

if get_option('tools')
    subdir('tools')
endif

if get_option('tests') or get_option('tests-case')!=''
    subdir('test')
endif
