import unreal

def new_level():
    ELL = unreal.EditorLevelLibrary()
    created = ELL.new_level("/Game/Levels/NewLevel")
    return created