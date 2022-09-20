root_include = include_directories('include')
common_include = include_directories('common')
core_include = include_directories('core')

# The include is added to each source file compiled on windows
if host_machine.system() == 'windows'
    add_project_arguments('-FI@0@\src\windows\include\platform.h'.format(meson.project_source_root()), language : 'c')
    add_project_arguments('-DPMDK_UTF8_API', language: 'c')
    windows_include = include_directories('windows/include')
else
    windows_include = ''
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
#subdir('examples')

if get_option('rpmem')
    #subdir('librpmem')
endif

if get_option('tools')
    #subdir('tools')
endif

if get_option('tests') or get_option('tests-case')!=''
    subdir('test')
endif
