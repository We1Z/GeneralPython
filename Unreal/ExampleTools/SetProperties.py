import unreal


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


EdUtil = MyEditorUtility()

selectedAsset = EdUtil.get_selected_assets()

for asset in selectedAsset:
    asset.set_editor_property("BlueprintDisplayName", "Some BP")
    asset.set_editor_property("BlueprintDescription", "A general description text")
    asset.set_editor_property("BlueprintCategory", "Collectible")
    unreal.log("Blueprint display name changed")

selectedActor = EdUtil.get_selection_set()

for actor in selectedActor:
    actor.set_editor_property("bHidden", 1)
    actor.set_editor_property("EditorBillboardScale", 10)

