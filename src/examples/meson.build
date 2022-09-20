examples_include = include_directories('.')

subdir('libpmem')
subdir('libpmemblk')
subdir('libpmemlog')
subdir('libpmemobj')
subdir('libpmem2')
subdir('libpmemset')

if host_machine.system() != 'windows'
    subdir('libpmempool')
    subdir('pmreorder')
endif