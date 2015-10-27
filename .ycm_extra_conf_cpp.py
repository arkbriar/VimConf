import os
import ycm_core

# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.

# These are the compilation flags that will be used in case there's no
# compilation database set.
flags = [
'-Wall',
'-Wextra',
'-Werror',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
# THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
# language to use when compiling headers. So it will guess. Badly. So C++
# headers will be compiled as C headers. You don't want that so ALWAYS specify
# a "-std=<something>".
# For a C project, you would set this to something like 'c99' instead of
# 'c++11'.
'-std=c++11',
# ...and the same thing goes for the magic -x option which specifies the
# language that the files to be compiled are written in. This is mostly
# relevant for c++ headers.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
'-DQT_CORE_LIB',
'-DQT_GUI_LIB',
'-DQT_NETWORK_LIB',
'-DQT_QML_LIB',
'-DQT_QUICK_LIB',
'-DQT_SQL_LIB',
'-DQT_WIDGETS_LIB',
'-DQT_XML_LIB',

'-I', '/usr/include',
'-I', '/usr/include/c++/5',
'-I', '/usr/include/c++/5/x86_64-suse-linux',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/Enginio',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtBluetooth',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtCLucene',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtConcurrent',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtCore',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtDBus',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtDeclarative',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtDesigner',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtDesignerComponents',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtGui',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtHelp',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtLocation',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtMultimedia',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtMultimediaQuick_p',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtMultimediaWidgets',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtNetwork',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtNfc',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtOpenGL',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtOpenGLExtensions',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtPlatformHeaders',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtPlatformSupport',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtPositioning',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtPrintSupport',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtQml',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtQuick',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtQuickParticles',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtQuickTest',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtQuickWidgets',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtScript',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtScriptTools',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtSensors',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtSerialPort',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtSql',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtSvg',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtTest',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtUiTools',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebChannel',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebEngine',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebEngineWidgets',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebKit',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebKitWidgets',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebSockets',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWebView',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtWidgets',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtX11Extras',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtXml',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtXmlPatterns',
# '-I', '/home/homura/Qt5.4.2/5.4/gcc_64/include/QtZlib',

'-I', '.',
'-I', 'include',
'-I', 'test',
'-I', 'build',
'-I', 'build/debug',
'-I', 'build/release',
]

compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

    # NOTE: This is just for YouCompleteMe; it's highly likely that your project
    # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
    # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
    try:
      final_flags.remove( '-stdlib=libc++' )
    except ValueError:
      pass
  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
