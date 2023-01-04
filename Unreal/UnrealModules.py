import unreal

info = dir(unreal)

# finding all modules currently in unreal 4.27
for i in info:
    unreal.log("unreal." + str(i))
