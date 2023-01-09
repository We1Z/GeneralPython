import unreal

blueprintName = "MyEpicBPActorClass"
blueprintPath = "/Game/AutoCreated"

# right click in unreal and create BP
factory = unreal.BlueprintFactory()

# setting parent class
# factory is child to Object and is Child to ObjectBase
# set_editor_property is a function from ObjectBase
# set_editor_property(name, value)
factory.set_editor_property("ParentClass", unreal.Actor)

# Store assetTool
assetTools = unreal.AssetToolsHelpers().get_asset_tools()

# Created the asset
myFancyNewAssetFile = assetTools.create_asset(blueprintName, blueprintPath, None, factory)

# save asset created = click on save button
unreal.EditorAssetLibrary.save_loaded_asset(myFancyNewAssetFile)

