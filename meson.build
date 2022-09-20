project(
    'pmdk',
    ['c'],
    license: 'BSD-3-clause',
    version: '1.12.0',
    default_options: [
        'buildtype=debugoptimized',
        'c_std=gnu99',
	    'b_lto=false',
	    'buildtype=debug',
    ],
)

version_components = meson.project_version().split('.')

pmdk_major_version = version_components[0]
pmdk_minor_version = version_components[1]
pmdk_patch_version = version_components[2]

cc = meson.get_compiler('c')
cmake = import('cmake')

add_project_arguments(
    '-DSRCVERSION="@0@"'.format(meson.project_version()),
    language: 'c'
)

# The include can be found inside src/windows/include/platform.h header
# for windows build
if get_option('debug') and host_machine.system() != 'windows'
    add_project_arguments('-DDEBUG', language: 'c')
endif

flags = [
    '-fno-common',
    '-Wconversion',
    '-Wunreachable-code-return',
    '-Wmissing-variable-declarations',
    '-Wfloat-equal',
    '-Wswitch-default',
    '-Wcast-function-type',
    '-Wstringop-truncation',
]

add_project_arguments(cc.get_supported_arguments(flags), language: 'c')

fs = import('fs')

libdl_dep = cc.find_library('dl', required: false)
libm_dep = cc.find_library('m', required:false)

threads_dep = dependency('threads')
# TODO: Add wrap (autotools)
libndctl_dep = dependency('libndctl', version: '>= 63', required: get_option('ndctl'))
libdaxctl_dep = dependency('libdaxctl', version: '>= 63', required: get_option('ndctl'))
libfabric_dep = dependency('libfabric', version: '>= 1.4.2', required: false) # TODO: is it necessary?
libncurses_dep = dependency('ncurses', required: false)
libuv_dep = dependency('libuv', required: false)
libfuse_dep = dependency('fuse', version: '>= 2.9.1', required: false)

opt_var = cmake.subproject_options()
opt_var.add_cmake_defines({'BUILD_DOC': false})
opt_var.add_cmake_defines({'BUILD_EXAMPLES': false})
opt_var.add_cmake_defines({'BUILD_TESTS': false})
miniasync_proj = cmake.subproject('miniasync')
miniasync_dep = miniasync_proj.dependency('miniasync')

# Necessary due to a bug in cmake module that propagates
# PRIVATE target_link_args into link args, so flags
# such as /DEF would be added to targets depending
# on the miniasync_dep
miniasync_dep = miniasync_dep.partial_dependency( 
    compile_args : true,
    includes     : false,
    link_args    : false,
    links        : true,
    sources      : false,
)
miniasync_dep = declare_dependency(
    include_directories: include_directories('subprojects/miniasync/src/include'),
    dependencies: [miniasync_dep],
)

if libndctl_dep.found()
    add_project_arguments(
        '-DNDCTL_ENABLED=1',
        '-DSDS_ENABLED',
        language: 'c'
    )
endif

if host_machine.system()=='linux' and (get_option('doc') or get_option('web'))
    subdir('doc')
endif

subdir('src')

if get_option('tests')
    subdir('testsuite')
endif
