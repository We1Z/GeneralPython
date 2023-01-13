import unreal

# variables
newFileName = ""
# /Game/Content/Assets/Set/
templatePath = "/Game/Assets/Set/"

VT_fileCreatePath = templatePath


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MyAssetToolsHelper(unreal.AssetToolsHelpers):
    pass


# Shorten function name
EdUti = MyEditorUtility()
Factory = unreal.RuntimeVirtualTextureFactory()

# get selected level asset to find its name and path
selectedLevel = EdUti.get_selected_assets()

# For any asset creation in unreal content browser
AssetTools = MyAssetToolsHelper.get_asset_tools()


# Function will return a string of VT folder path
def makeCreatedPath():
    if len(selectedLevel) != 0:
        for assetLevel in selectedLevel:
            # Get the string of the level path
            # goldenDeliciousPark_Winter_Market_EXT_Level
            FileName = assetLevel.get_name()

            newVT_rootPath = (templatePath + FileName).replace("_Level", "")
            unreal.log("File will be created in " + newVT_rootPath)

            return newVT_rootPath

    else:
        return unreal.log_error("No asset selected for VT file generation")


# VT_fileCreatePath = makeCreatedPath()
# unreal.log_warning(VT_fileCreatePath)

# This function will first create VT folder and then create two RVT files into VT folder
def CreateVT():
    newVT_FileName = (selectedLevel[0].get_name()).replace("_EXT_Level", "")
    # unreal.log(newVT_FileName)


    new_VT_FileCreatePath = VT_fileCreatePath + newVT_FileName + "_EXT/VT/"
    # unreal.log(new_VT_FileCreatePath)

    # Create VT folder
    unreal.EditorAssetLibrary.make_directory(new_VT_FileCreatePath)

    checkMATFileNamePath = new_VT_FileCreatePath + "VT_" + newVT_FileName + "_Mat"
    checkHeightFileNamePath = new_VT_FileCreatePath + "VT_" + newVT_FileName + "_Height"

    # check if VT_Mat file has been already created
    if unreal.EditorAssetLibrary.does_asset_exist(checkMATFileNamePath):
        unreal.log_error("VT file Mat has already created")
    else:
        # create Mat VT file
        MyVTNewFile = AssetTools.create_asset("VT_" + newVT_FileName + "_Mat", new_VT_FileCreatePath, None, Factory)

        # Load the asset and change Tile Count to 10 so its 1024
        VT_Mat_Object = unreal.EditorAssetLibrary.load_asset(checkMATFileNamePath)
        VT_Mat_Object.set_editor_property("TileCount", 10)

        # Save the asset
        unreal.EditorAssetLibrary.save_loaded_asset(MyVTNewFile)
        unreal.log("Mat VT created")

    # check if VT_Height file has been already created
    if unreal.EditorAssetLibrary.does_asset_exist(checkHeightFileNamePath):
        unreal.log_error("VT file Height has already created")
    else:
        MyVTNewFile2 = AssetTools.create_asset("VT_" + newVT_FileName + "_Height", new_VT_FileCreatePath, None, Factory)

        # Load the asset and change Tile Count to 10 so its 1024
        VT_Height_Object = unreal.EditorAssetLibrary.load_asset(checkHeightFileNamePath)
        VT_Height_Object.set_editor_property("TileCount", 10)

        # Change the material type to using World Height for VT_height
        heightEnumProperty = unreal.RuntimeVirtualTextureMaterialType.WORLD_HEIGHT
        VT_Height_Object.set_editor_property("material_type", heightEnumProperty)

        # Save the asset
        unreal.EditorAssetLibrary.save_loaded_asset(MyVTNewFile2)
        unreal.log("Height VT created")



# only if there is a level assets selected then run the function to create VTss

checkSelectedClass = selectedLevel[0].get_class()

checkAgainstName = unreal.World().get_class()

unreal.log_warning(checkSelectedClass)

if str(checkAgainstName) in str(checkSelectedClass):
    unreal.log_error(str(checkSelectedClass))
    CreateVT()
else:
    unreal.log_error("False statement")
    unreal.log_warning("Please select a level and retry")
#


