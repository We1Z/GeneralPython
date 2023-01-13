import unreal


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


# get the current level
currentLevel = unreal.EditorLevelLibrary.get_editor_world()

# select all the actors in the level
actorsFromWorld = unreal.EditorLevelLibrary.get_all_level_actors()

# selected assets from the content browser
selectedAssets = MyEditorUtility().get_selected_assets()

actorNameToFilter = "RuntimeVirtualTexture_"
containFunction = unreal.EditorScriptingStringMatchType.CONTAINS
includesType = unreal.EditorScriptingFilterType.INCLUDE
# Filter through all the actors to get the RVT volume actor
filteredActor = unreal.EditorFilterLibrary.by_actor_label(actorsFromWorld, actorNameToFilter, containFunction,
                                                          includesType)

# Select first and second RVT
firstActor = filteredActor[0]
secondActor = filteredActor[1]
# set property of VirtureTexture to RuntimeVirtualTexture file
VirtualTexture = unreal.RuntimeVirtualTextureComponent.virtual_texture

# file selected from unreal content browser
selectedAssets[0]
selectedAssets[1]



# printing all the assets been selected from the unreal content browser
for asset in selectedAssets:
    assetName = asset.get_name()
    unreal.log(assetName)

# printing all the actors from the world outline
for actor in actorsFromWorld:
    actorName = actor.get_name()
    unreal.log(actorName)
