# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB

# Include any dependencies generated for this target.
include example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/depend.make

# Include the progress variables for this target.
include example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/progress.make

# Include the compile flags for this target's objects.
include example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/flags.make

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/flags.make
example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o: example/approxMVBB/src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o"
	cd /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o -c /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB/src/main.cpp

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.i"
	cd /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB/src/main.cpp > CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.i

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.s"
	cd /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB/src/main.cpp -o CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.s

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.requires:

.PHONY : example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.requires

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.provides: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.requires
	$(MAKE) -f example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/build.make example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.provides.build
.PHONY : example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.provides

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.provides.build: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o


# Object files for target ApproxMVBBExample
ApproxMVBBExample_OBJECTS = \
"CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o"

# External object files for target ApproxMVBBExample
ApproxMVBBExample_EXTERNAL_OBJECTS =

example/approxMVBB/ApproxMVBBExample: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o
example/approxMVBB/ApproxMVBBExample: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/build.make
example/approxMVBB/ApproxMVBBExample: lib/libApproxMVBB.so.2.0.1
example/approxMVBB/ApproxMVBBExample: /usr/local/lib/libpugixml.a
example/approxMVBB/ApproxMVBBExample: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ApproxMVBBExample"
	cd /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ApproxMVBBExample.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/build: example/approxMVBB/ApproxMVBBExample

.PHONY : example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/build

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/requires: example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/src/main.cpp.o.requires

.PHONY : example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/requires

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/clean:
	cd /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB && $(CMAKE_COMMAND) -P CMakeFiles/ApproxMVBBExample.dir/cmake_clean.cmake
.PHONY : example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/clean

example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/depend:
	cd /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB /home/taihu/Documentos/jcorti_bkp/ApproxMVBB2/ApproxMVBB/example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : example/approxMVBB/CMakeFiles/ApproxMVBBExample.dir/depend

