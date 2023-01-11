import unreal


def createRVTVol(count):
    for i in range(count):
        RVT_VolActor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.RuntimeVirtualTextureVolume,
                                                                        unreal.Vector(0, 0, 0),
                                                                        unreal.Rotator(0, 0, 0), False)
        newName = RVT_VolActor.set_editor_property("DisplayName", f"Vol{i}")
        unreal.log(newName)


createRVTVol(2)
