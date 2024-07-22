import shutil
import platform
from pathlib import Path

HOST = platform.system()
if HOST == "Linux":
    os = 'glnxa64'
    ext = 'so'
    static_ext = 'a'
    MATLABROOT = "/usr/local/MATLAB"
elif HOST == "Windows":
    os = 'win64'
    ext = 'dll'
    static_ext = 'lib'
    MATLABROOT = "C:/Program Files/MATLAB"
else:
    print("unreachable")
R2016a = "R2016a"
R2016b = "R2016b"
R2017a = "R2017a"
R2017b = "R2017b"
R2018a = "R2018a"
R2018b = "R2018b"
R2019a = "R2019a"
R2019b = "R2019b"
R2020a = "R2020a"
R2020b = "R2020b"
R2021a = "R2021a"
R2021b = "R2021b"
R2022a = "R2022a"
R2022b = "R2022b"
R2023a = "R2023a"
R2023b = "R2023b"

grp_all = [
    R2016a,
    R2016b,
    R2017a,
    R2017b,
    R2018a,
    R2018b,
    R2019a,
    R2019b,
    R2020a,
    R2020b,
    R2021a,
    R2021b,
    R2022a,
    R2022b,
    R2023a,
    R2023b,
]

def try_copytree(src, dst):
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except Exception as e:
        print(e)

def try_copy(src, dst):
    Path(dst).resolve().parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copyfile(src, dst)
    except Exception as e:
        print(e)



for ver in grp_all:
    try_copy(f"{MATLABROOT}/{ver}/extern/lib/win64/mingw64/libmx.lib",              f"./{ver}/extern/lib/win64/mingw64/libmx.lib")
    try_copy(f"{MATLABROOT}/{ver}/extern/lib/win64/mingw64/libmat.lib",             f"./{ver}/extern/lib/win64/mingw64/libmat.lib")
    try_copy(f"{MATLABROOT}/{ver}/extern/lib/win64/mingw64/libmex.lib",             f"./{ver}/extern/lib/win64/mingw64/libmex.lib")
    try_copy(f"{MATLABROOT}/{ver}/extern/lib/win64/mingw64/libut.lib",              f"./{ver}/extern/lib/win64/mingw64/libut.lib")
    try_copy(f"{MATLABROOT}/{ver}/extern/lib/win64/mingw64/libfixedpoint.lib",      f"./{ver}/extern/lib/win64/mingw64/libfixedpoint.lib")
    try_copy(f"{MATLABROOT}/{ver}/bin/win64/libmx.dll",                             f"./{ver}/bin/win64/libmx.dll")
    try_copy(f"{MATLABROOT}/{ver}/bin/win64/libmat.dll",                            f"./{ver}/bin/win64/libmat.dll")
    try_copy(f"{MATLABROOT}/{ver}/bin/win64/libmex.dll",                            f"./{ver}/bin/win64/libmex.dll")
    try_copy(f"{MATLABROOT}/{ver}/bin/win64/libut.dll",                             f"./{ver}/bin/win64/libut.dll")
    try_copy(f"{MATLABROOT}/{ver}/bin/win64/libfixedpoint.dll",                     f"./{ver}/bin/win64/libfixedpoint.dll")
    try_copy(f"{MATLABROOT}/{ver}/bin/win64/scanutil.dll",                          f"./{ver}/bin/win64/scanutil.dll")
    try_copy(f"{MATLABROOT}/{ver}/bin/glnxa64/libmx.so",                            f"./{ver}/bin/glnxa64/libmx.so")
    try_copy(f"{MATLABROOT}/{ver}/bin/glnxa64/libmat.so",                           f"./{ver}/bin/glnxa64/libmat.so")
    try_copy(f"{MATLABROOT}/{ver}/bin/glnxa64/libmex.so",                           f"./{ver}/bin/glnxa64/libmex.so")
    try_copy(f"{MATLABROOT}/{ver}/bin/glnxa64/libut.so",                            f"./{ver}/bin/glnxa64/libut.so")
    try_copy(f"{MATLABROOT}/{ver}/bin/glnxa64/libfixedpoint.so",                    f"./{ver}/bin/glnxa64/libfixedpoint.so")
    try_copy(f"{MATLABROOT}/{ver}/bin/glnxa64/libmwscanutil.so",                    f"./{ver}/bin/glnxa64/libmwscanutil.so")
    try_copytree(f"{MATLABROOT}/{ver}/extern/include",                              f"./{ver}/extern/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/version",                              f"./{ver}/extern/version")
    try_copytree(f"{MATLABROOT}/{ver}/simulink/include",                            f"./{ver}/simulink/include")
    try_copytree(f"{MATLABROOT}/{ver}/rtw/c/src",                                   f"./{ver}/rtw/c/src")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/vnt/vntblks",                         f"./{ver}/toolbox/vnt/vntblks")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/shared/can/src/scanutil",             f"./{ver}/toolbox/shared/can/src/scanutil")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ex/include",              f"./{ver}/extern/physmod/{os}/ex/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ex/lib",                  f"./{ver}/extern/physmod/{os}/ex/lib")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/lang/include",            f"./{ver}/extern/physmod/{os}/lang/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/mc/include",              f"./{ver}/extern/physmod/{os}/mc/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/mc/lib",                  f"./{ver}/extern/physmod/{os}/mc/lib")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/pm/include",              f"./{ver}/extern/physmod/{os}/pm/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/pm/lib",                  f"./{ver}/extern/physmod/{os}/pm/lib")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/pm_log/include",          f"./{ver}/extern/physmod/{os}/pm_log/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_comp/include",        f"./{ver}/extern/physmod/{os}/ssc_comp/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_core/include",        f"./{ver}/extern/physmod/{os}/ssc_core/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_core/lib",            f"./{ver}/extern/physmod/{os}/ssc_core/lib")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_ds/include",          f"./{ver}/extern/physmod/{os}/ssc_ds/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_sli/include",         f"./{ver}/extern/physmod/{os}/ssc_sli/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_sli/lib",             f"./{ver}/extern/physmod/{os}/ssc_sli/lib")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_st/include",          f"./{ver}/extern/physmod/{os}/ssc_st/include")
    try_copytree(f"{MATLABROOT}/{ver}/extern/physmod/{os}/ssc_st/lib",              f"./{ver}/extern/physmod/{os}/ssc_st/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/external/library/c",   f"./{ver}/toolbox/physmod/common/external/library/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/external/library/lib", f"./{ver}/toolbox/physmod/common/external/library/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/foundation/core/c",    f"./{ver}/toolbox/physmod/common/foundation/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/foundation/core/lib",  f"./{ver}/toolbox/physmod/common/foundation/core/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/lang/core/c",          f"./{ver}/toolbox/physmod/common/lang/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/logging/core/c",       f"./{ver}/toolbox/physmod/common/logging/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/math/core/c",          f"./{ver}/toolbox/physmod/common/math/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/common/math/core/lib",        f"./{ver}/toolbox/physmod/common/math/core/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/drive/c",                     f"./{ver}/toolbox/physmod/drive/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/drive/lib",                   f"./{ver}/toolbox/physmod/drive/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/extern/include",              f"./{ver}/toolbox/physmod/extern/include")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/network_engine/c",            f"./{ver}/toolbox/physmod/network_engine/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/network_engine/lib",          f"./{ver}/toolbox/physmod/network_engine/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/pm_math/c",                   f"./{ver}/toolbox/physmod/pm_math/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/pm_math/lib",                 f"./{ver}/toolbox/physmod/pm_math/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/compiler/core/c",    f"./{ver}/toolbox/physmod/simscape/compiler/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/ds/core/c",          f"./{ver}/toolbox/physmod/simscape/ds/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/engine/core/c",      f"./{ver}/toolbox/physmod/simscape/engine/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/engine/core/lib",    f"./{ver}/toolbox/physmod/simscape/engine/core/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/engine/sli/c",       f"./{ver}/toolbox/physmod/simscape/engine/sli/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/engine/sli/lib",     f"./{ver}/toolbox/physmod/simscape/engine/sli/lib")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/simtypes/core/c",    f"./{ver}/toolbox/physmod/simscape/simtypes/core/c")
    try_copytree(f"{MATLABROOT}/{ver}/toolbox/physmod/simscape/simtypes/core/lib",  f"./{ver}/toolbox/physmod/simscape/simtypes/core/lib")
