import unreal

# getting some pre-required info for what we are doing
# Creating 20 BP, so we have a variable int called totalRequiredBP
totalRequiredBP = 20
# Store the new BP name as variant that we can increment the suffix with %d and latter modified it
newAssetsName = "BP_PythonMade_%d"
# Store the path of the new BPs that is gonna create into a variable
createAssetsPath = "/Game/Test"
# A variable that display info during slowscopedtask
slowTaskDisplayText = "Creating New Assets..."

# called BlueprintFactory() = right-clicking in content browser to create new BP inside unreal
factory = unreal.BlueprintFactory()
# selecting which class the BP is going to inherit from, the following example is inherting from Actor class
factory.set_editor_property("ParentClass", unreal.Actor)

# We need AssetsToolHelpers to create new assets
assetTools = unreal.AssetToolsHelpers.get_asset_tools()

# unreal.ScopedSlowTask will prompt loading screen insdie Unreal showing something is happening or it may feel nothing
# has happened when the code is exceuting.
with unreal.ScopedSlowTask(totalRequiredBP, slowTaskDisplayText) as ST:
    # make_dialog will prompt the loading to show
    ST.make_dialog(True)
    # looping in how many BP we are creating
    for x in range(totalRequiredBP):
        # checking if user want to cancel the operation in the middle of the looping
        if ST.should_cancel():
            break
        # create assset function and given the name and path we want
        newAsset = assetTools.create_asset(newAssetsName%(x), createAssetsPath, None, factory)

        # EditorAssetLibrary are need to save the newly created BP assets
        unreal.EditorAssetLibrary.save_loaded_asset(newAsset)

        # Pring out all newly created BP assets
        unreal.log("Just created an asset BP_PythonMade_%d via PYTHON API" %(x))

        # Have the progress bar move as one asset creation is finished
        ST.enter_progress_frame(1)


