import unreal
import sys

# total of material instance that will be created
# totalRequiredInstances = 10
totalRequiredInstances = int(sys.argv[1])

# some variable needed for functions to work
newAssetName = ""
sourceAssetPath = ""
createdAssetPath = ""


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MyMaterialEditingLibrary(unreal.MaterialEditingLibrary):
    pass


# make class names shorter
editorUtil = MyEditorUtility()
materialEditingLib = MyMaterialEditingLibrary()

# get all selected asset in content browser
selectedAssets = editorUtil.get_selected_assets()

# called factory that create material instances
factor = unreal.MaterialInstanceConstantFactoryNew()
#  called asset creater tool for unreal
assetTool = unreal.AssetToolsHelpers.get_asset_tools()

#
for selectAsset in selectedAssets:
    # getting the name and file path of the assets that need to create instances
    newAssetName = selectAsset.get_name() + "_%s_%d"
    sourceAssetPath = selectAsset.get_path_name()
    # Generating file path same as the parent material path, with python replace() function
    createdAssetPath = sourceAssetPath.replace(selectAsset.get_name(), "-")
    createdAssetPath = createdAssetPath.replace("-.-", "")

    for x in range(totalRequiredInstances):
        newAsset = assetTool.create_asset(newAssetName % ("inst", x + 1,), createdAssetPath, None, factor)
        materialEditingLib.set_material_instance_parent(newAsset, selectAsset)

