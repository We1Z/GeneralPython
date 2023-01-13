import unreal

# the amount of runtime virtual texture is going need to create
createCount = 2
currentLevel = unreal.EditorLevelLibrary.get_editor_world()

def createRVTVol(count=None, world=None):
    world = world if world is not None else unreal.EditorLevelLibrary.get_editor_world()  # make sure there is a valid level

    for i in range(count):
        RVT_Volume = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.RuntimeVirtualTextureVolume,
                                                                      unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0),
                                                                      False)

        if i == 0:
            RVT_Volume.set_actor_label("RuntimeVirtualTexture_Mat")
        elif i == 1:
            RVT_Volume.set_actor_label("RuntimeVirtualTexture_Height")
        else:
            unreal.log_error("Currently a Max of two volume can be generated at a time")




createRVTVol(createCount, currentLevel)
