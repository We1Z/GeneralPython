import unreal

# variables
newFileName = ""

VT_fileCreatePath = ""


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MyAssetToolsHelper(unreal.AssetToolsHelpers):
    pass


EdUti = MyEditorUtility()
Factory = unreal.RuntimeVirtualTextureFactory()
selectedLevel = EdUti.get_selected_assets()


def makeCreatedPath():
    # /Game/Content/Assets/Set/
    templatePath = "/Game/Assets/Set/"

    selectedLevel = EdUti.get_selected_assets()
    if len(selectedLevel) != 0:
        for assetLevel in selectedLevel:
            # goldenDeliciousPark_Winter_Market_EXT_Level
            FileName = assetLevel.get_name()
            unreal.log(FileName)

            newVT_rootPath = (templatePath + FileName).replace("_Level", "")
            unreal.log(newVT_rootPath)

            return newVT_rootPath

    else:
        return unreal.log_error("No asset selected for VT file generation")


VT_fileCreatePath = makeCreatedPath()
unreal.log_warning(VT_fileCreatePath)


def CreateVT():
    newVT_FileName = (selectedLevel[0].get_name()).replace("_EXT_Level", "")
    unreal.log(newVT_FileName)
    new_VT_FileCreatePath = VT_fileCreatePath + "/VT/"
    unreal.log(new_VT_FileCreatePath)

    unreal.EditorAssetLibrary.make_directory(new_VT_FileCreatePath)
    AssetTools = MyAssetToolsHelper.get_asset_tools()
    checkMATFileNamePath = new_VT_FileCreatePath + "VT_" + newVT_FileName + "_Mat"
    checkHeightFileNamePath = new_VT_FileCreatePath + "VT_" + newVT_FileName + "_Height"


    if unreal.EditorAssetLibrary.does_asset_exist(checkMATFileNamePath):
        unreal.log_error("VT file Mat has already created")
    else:
        MyVTNewFile = AssetTools.create_asset("VT_" + newVT_FileName + "_Mat", new_VT_FileCreatePath, None, Factory)
        VT_Mat_Object = unreal.EditorAssetLibrary.load_asset(checkMATFileNamePath)

        VT_Mat_Object.set_editor_property("TileCount", 10)



        unreal.EditorAssetLibrary.save_loaded_asset(MyVTNewFile)
        unreal.log("Mat VT created")

    if unreal.EditorAssetLibrary.does_asset_exist(checkHeightFileNamePath):
        unreal.log_error("VT file Height has already created")
    else:
        MyVTNewFile2 = AssetTools.create_asset("VT_" + newVT_FileName + "_Height", new_VT_FileCreatePath, None, Factory)
        VT_Height_Object = unreal.EditorAssetLibrary.load_asset(checkHeightFileNamePath)
        VT_Height_Object.set_editor_property("TileCount", 10)

        heightEnumProperty = unreal.RuntimeVirtualTextureMaterialType.WORLD_HEIGHT

        VT_Height_Object.set_editor_property("material_type", heightEnumProperty)

        unreal.EditorAssetLibrary.save_loaded_asset(MyVTNewFile2)
        unreal.log("Height VT created")









if len(selectedLevel) != 0:
    CreateVT()

else:
    unreal.log_warning("Please select a level and retry")
