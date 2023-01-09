import unreal


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

# get a list of selected assets from content browser
selectedAssets = MyEditorUtility().get_selected_assets()
# store some name and path of the seleceted assets
assetPathName = selectedAssets[0].get_path_name()
selectedBPName = selectedAssets[0].get_name()

# loaded the selected assets
bp_asset = unreal.load_asset(assetPathName)

# Could also just enter the path of the assets for specific files, see below line
# bp_asset = unreal.load_asset( '/Game/BP_myblueprint' )

# get the root data handle, only apply in Unreal 5
subsystem: unreal.SubobjectDataSubsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
root_data_handle: unreal.SubobjectDataHandle = subsystem.k2_gather_subobject_data_for_blueprint(context=bp_asset)

# created a empty container for data coming from the handles
objects = []


# get components in blueprint and added them to the object container
for handle in root_data_handle:
    subobject = subsystem.k2_find_subobject_data_from_handle(handle)
    objects.append(unreal.SubobjectDataBlueprintFunctionLibrary.get_object(subobject))

# get a list of the components (full name)
objects = list(dict.fromkeys(objects))

#unreal.log_warning(objects)

# check if StaticMeshComponent is in the BP and check the static_mesh parameter
for x in objects:
    if "StaticMeshComponent" in str(x):
        static_mesh = x.get_editor_property("static_mesh")
        simpleName = static_mesh.get_name()
        unreal.log_error("The {0} has {1} as static mesh".format(selectedBPName, simpleName))

        if str(static_mesh) == "None":
            unreal.log("StaticMeshComponent: " + str(x) + " has no static_mesh")

