ttools = {
    'bttcreate': {},
    'cmpmap': {},
    'cpufd': {},
    'ddmap': {},
    'gran_detecto': {},
    'pmemalloc': {},
    'pmemdetect': {},
    'pmemobjcli': {},
    'pmemspoil': {},
    'pmemwrite': {},
}

if host_machine.system() != 'windows'
    ttools += {
        'anonymous_mmap': {},
        'ctrld': {},
        'extents': {},
        'fallocate_detect': {},
        'mapexec': {},
        'obj_verify': {},
        'usc_permission_check': {},
    }
else
    ttools += {
        'dllview': {},
        'sparsefile': {},
    }
endif

# This dependency is quite rough, but that's the way
# it was in src/tools/Makefile.inc
tools_common = static_library(
    'tools_common',
    objects:[pmempool.extract_objects('pmempool/common.c', 'pmempool/output.c'),
            libpmemblk.extract_objects('btt.c'),
        ],
    install:false
)

tools_common_dep = declare_dependency(
    link_whole: tools_common,
    dependencies: [pmemcommon_dep,
            pmemcore_dep,
        ],
    include_directories:[
        '../../src/tools/pmempool',
        '../../src/core',
        '../../src/common',
        '../../src/libpmemlog',
        '../../src/libpmemblk',
        '../../src/libpmemobj'
        ],
)

foreach ttool, args : ttools
    subdir(ttool)
endforeach
